# GNR638 Project 2: Deep Learning MCQ Image Answering

This project predicts answers for PNG images containing deep-learning multiple-choice questions.

## Method

The inference pipeline is:

1. Read `test.csv` from the `--test_dir` argument.
2. Read each image from `--test_dir/images`.
3. OCR the image using Tesseract.
4. Feed the extracted text to a TinyLlama LoRA adapter.
5. Write `submission.csv` in the current project directory.

The submitted answer format is:

```csv
image_name,option
image_1,1
image_2,5
```

Options are mapped as:

- `1` = A
- `2` = B
- `3` = C
- `4` = D
- `5` = unanswered / unsure

## Files

```text
inference.py
tinyllama_mcq_lora/
```

`setup.bash` in the Moodle zip fetches these files from this repository folder and downloads the TinyLlama base model during setup.

## Grading Command

```bash
python inference.py --test_dir <absolute_path_to_test_dir>
```

The script writes:

```text
submission.csv
```

in the current directory.
