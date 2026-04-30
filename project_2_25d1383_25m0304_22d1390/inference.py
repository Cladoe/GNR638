#!/usr/bin/env python3
"""Inference for OCR + TinyLlama/Phi-2 LoRA MCQ answering.

The grader will run:
    python inference.py --test_dir <absolute_path_to_test_dir>

This script writes submission.csv in the current project directory.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
from pathlib import Path

os.environ.setdefault("PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION", "python")
os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
os.environ.setdefault("TRANSFORMERS_NO_FLAX", "1")
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

import torch
from PIL import Image, ImageEnhance, ImageFilter
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

try:
    import pytesseract
except Exception:
    pytesseract = None


SYSTEM_INSTRUCTION = (
    "You answer deep learning multiple-choice questions. "
    "Options are labeled A, B, C, and D. "
    "Return only one number: 1 for A, 2 for B, 3 for C, 4 for D, or 5 if unsure."
)


def build_prompt(mcq_text: str) -> str:
    return (
        f"### Instruction:\n{SYSTEM_INSTRUCTION}\n\n"
        f"### Question:\n{mcq_text.strip()}\n\n"
        "### Answer:\n"
    )


def extract_option(text: str) -> int:
    match = re.search(r"\b[1-5]\b", str(text))
    if match:
        return int(match.group(0))
    match = re.search(r"[1-5]", str(text))
    return int(match.group(0)) if match else 5


def preprocess_for_ocr(image_path: Path) -> Image.Image:
    image = Image.open(image_path).convert("L")
    width, height = image.size
    if max(width, height) < 2200:
        image = image.resize((width * 2, height * 2))
    image = ImageEnhance.Contrast(image).enhance(1.8)
    return image.filter(ImageFilter.SHARPEN)


def ocr_image(image_path: Path) -> str:
    if pytesseract is None:
        return ""
    try:
        image = preprocess_for_ocr(image_path)
        text = pytesseract.image_to_string(image, config="--psm 6")
        return re.sub(r"\n{3,}", "\n\n", text).strip()
    except Exception:
        return ""


def find_image_path(image_dir: Path, image_name: str) -> Path:
    raw = Path(str(image_name).strip())
    if raw.suffix:
        candidates = [image_dir / raw.name]
    else:
        candidates = [
            image_dir / f"{image_name}.png",
            image_dir / f"{image_name}.jpg",
            image_dir / f"{image_name}.jpeg",
            image_dir / image_name,
        ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def load_model(project_dir: Path):
    model_candidates = [
        project_dir / "TinyLlama-1.1B-Chat-v1.0",
        Path("/home/aditig/wheels/TinyLlama-1.1B-Chat-v1.0"),
        project_dir / "phi-2",
        Path("/home/aditig/wheels/phi-2"),
    ]
    adapter_candidates = [
        project_dir / "tinyllama_mcq_lora",
        project_dir / "phi2_mcq_lora",
    ]

    base_model = next((p for p in model_candidates if p.exists()), None)
    adapter = next((p for p in adapter_candidates if p.exists()), None)
    if base_model is None:
        raise FileNotFoundError("No local TinyLlama/Phi-2 model folder found.")
    if adapter is None:
        raise FileNotFoundError("No LoRA adapter folder found.")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    tokenizer = AutoTokenizer.from_pretrained(adapter, local_files_only=True, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    base = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=dtype,
        local_files_only=True,
        trust_remote_code=True,
    ).to(device)
    model = PeftModel.from_pretrained(base, adapter)
    model.eval()
    return model, tokenizer, device


def predict_text(model, tokenizer, device: str, text: str) -> int:
    if not text.strip():
        return 5
    prompt = build_prompt(text)
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)
    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=4,
            do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
    new_tokens = output_ids[0, inputs["input_ids"].shape[1] :]
    decoded = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
    return extract_option(decoded)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_dir", type=Path, required=True)
    args = parser.parse_args()

    project_dir = Path.cwd()
    test_csv = args.test_dir / "test.csv"
    image_dir = args.test_dir / "images"
    output = project_dir / "submission.csv"

    model, tokenizer, device = load_model(project_dir)

    rows = []
    with test_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            image_name = row.get("image_name") or row.get("image_id") or row.get("id")
            if not image_name:
                continue
            image_path = find_image_path(image_dir, image_name)
            text = ocr_image(image_path) if image_path.exists() else ""
            option = predict_text(model, tokenizer, device, text)
            rows.append({"image_name": image_name, "option": option})
            print(f"{image_name}: {option}")

    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["image_name", "option"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
