# GNR638 Assignment 1: Custom Deep Learning Framework

A lightweight CNN framework built from scratch using only Python standard libraries and OpenCV.

## Overview

This project implements a custom deep learning framework without using NumPy, PyTorch, or TensorFlow. It features a MobileNet-inspired architecture with depthwise separable convolutions for efficient image classification.

## Features

- **Pure Python Implementation**: No ML libraries (NumPy, PyTorch, TensorFlow)
- **Depthwise Separable Convolutions**: 25× reduction in MACs compared to standard CNNs
- **Fast Training**: Completes within 30 minutes per dataset
- **Two Datasets**: 10-class and 97-class image classification

## Results

| Dataset | Classes | Test Accuracy | Training Time |
|---------|---------|---------------|---------------|
| Dataset 1 | 10 | 72.88% | 29.0 min |
| Dataset 2 | 97 | 5.48% | 29.7 min |

## Architecture

```
Input (32×32×3)
  ↓
MaxPool (16×16×3)
  ↓
DepthwiseConv 3×3 (16×16×3)
  ↓
PointwiseConv 1×1 (16×16×2)
  ↓
ReLU
  ↓
MaxPool (8×8×2)
  ↓
Flatten (128)
  ↓
Dense → Softmax (n_classes)
```

**Parameters**: 1,328 (10 classes) | 12,551 (97 classes)  
**MACs**: 9,728 (10 classes) | 20,864 (97 classes)

## Installation

```bash
pip install opencv-python
```

## Usage

### Training

```bash
python train.py --data_path /path/to/dataset --epochs 2 --batch_size 256 --lr 0.08
```

### Evaluation

```bash
python evaluate.py --data_path /path/to/dataset --model_path model.pkl
```

### Jupyter Notebook

For a complete walkthrough, see `assignment01_final_codes.ipynb`

## File Structure

```
gnr638_assignment01/
├── train.py                  # Training script
├── evaluate.py               # Evaluation script
├── model.py                  # Model architecture
├── layers.py                 # Layer implementations
├── utils.py                  # Helper functions
├── assignment01_final_codes.ipynb  # Complete notebook
├── README.md                 # This file
└── requirements.txt          # Dependencies
```

## Technical Details

- **Optimizer**: SGD with learning rate 0.08
- **Batch Size**: 256
- **Epochs**: 2
- **Data Augmentation**: None (pure training)
- **Gradient Clipping**: ±10 for stability

## Acknowledgments

- Based on MobileNets architecture (Howard et al., 2017)
- Course: GNR638 - Machine Learning for Remote Sensing II
- Institution: IIT Bombay

## License

This project is for educational purposes as part of GNR638 coursework.
