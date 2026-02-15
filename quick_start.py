#!/usr/bin/env python3
"""
Quick Start Example for GNR638 Assignment 1

This script demonstrates how to use the framework with minimal setup.
For full training, use the Jupyter notebook: assignment01_final_codes.ipynb
"""

import cv2
import os
import time
import random

def load_image(path):
    """Load and preprocess a single image."""
    img = cv2.imread(path)
    if img is None:
        return None
    img = cv2.resize(img, (32, 32))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.normalize(img.astype('float32'), None, 0.0, 1.0, cv2.NORM_MINMAX)
    # Convert to list format (3D: channels x height x width)
    return [[list(map(float, img[i, :, c])) for i in range(32)] for c in range(3)]


def main():
    """Quick demonstration of image loading."""
    
    print("="*70)
    print("GNR638 Assignment 1 - Quick Start Example")
    print("="*70)
    
    # Example: Load a single image
    print("\nThis is a demonstration script.")
    print("For complete training, please use: assignment01_final_codes.ipynb")
    
    print("\nQuick facts about the framework:")
    print("  • Pure Python implementation (no NumPy/PyTorch)")
    print("  • MobileNet-inspired architecture")
    print("  • Training time: ~30 minutes per dataset")
    print("  • Parameters: 1,328 (10 classes) | 12,551 (97 classes)")
    print("  • MACs: 9,728 (10 classes) | 20,864 (97 classes)")
    
    print("\n" + "="*70)
    print("Setup Instructions:")
    print("="*70)
    print("1. Install dependencies:")
    print("   pip install -r requirements.txt")
    print("\n2. Configure your data paths in config.py")
    print("\n3. Open the Jupyter notebook:")
    print("   jupyter notebook assignment01_final_codes.ipynb")
    print("\n4. Run all cells to train and evaluate")
    
    print("\n" + "="*70)
    print("For detailed usage, see USAGE.md")
    print("="*70)


if __name__ == "__main__":
    main()
