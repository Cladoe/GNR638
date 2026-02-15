# Usage Guide

## Quick Start

### 1. Installation

```bash
git clone https://github.com/yourusername/gnr638_assignment01.git
cd gnr638_assignment01
pip install -r requirements.txt
```

### 2. Dataset Setup

Organize your datasets as follows:

```
data/
├── dataset1/
│   ├── train/
│   │   ├── class_0/
│   │   ├── class_1/
│   │   └── ...
│   └── test/
│       ├── class_0/
│       ├── class_1/
│       └── ...
└── dataset2/
    ├── train/
    └── test/
```

### 3. Configuration

Edit `config.py` to set your dataset paths:

```python
DATA_PATH_1 = '/path/to/dataset1/'
DATA_PATH_2 = '/path/to/dataset2/'
```

### 4. Running the Notebook

The easiest way to train and evaluate is using the Jupyter notebook:

```bash
jupyter notebook assignment01_final_codes.ipynb
```

Then run all cells in order.

## Understanding the Code

### Architecture

The model uses a MobileNet-inspired design:

1. **Early Pooling**: Reduces spatial dimensions from 32×32 to 16×16
2. **Depthwise Convolution**: Learns spatial features per channel
3. **Pointwise Convolution**: Mixes channel information
4. **ReLU Activation**: Non-linearity
5. **Max Pooling**: Further reduces to 8×8
6. **Flatten**: Converts to 1D vector
7. **Dense Layer**: Classification

### Key Features

- **No NumPy/PyTorch**: Pure Python implementation
- **Efficient**: 25× fewer MACs than standard CNNs
- **Fast Training**: ~30 minutes per dataset
- **Gradient Clipping**: Prevents exploding gradients

## Training Process

### Dataset 1 (10 classes)

```bash
# In the notebook, modify the path variable:
path = '/path/to/dataset1/'

# Expected results:
# - Training time: ~29 minutes
# - Test accuracy: ~72-73%
# - Total parameters: 1,328
```

### Dataset 2 (97 classes)

```bash
# In the notebook, modify the path variable:
path = '/path/to/dataset2/'

# Expected results:
# - Training time: ~30 minutes
# - Test accuracy: ~5-6%
# - Total parameters: 12,551
```

## Hyperparameter Tuning

You can modify these in `config.py`:

- `LEARNING_RATE`: Default 0.08 (try 0.05-0.1)
- `BATCH_SIZE`: Default 256 (adjust based on memory)
- `EPOCHS`: Default 2 (can increase if time permits)
- `NUM_FILTERS`: Default 4 (2-8 filters work well)

## Troubleshooting

### Out of Memory

Reduce `BATCH_SIZE` in `config.py`:

```python
BATCH_SIZE = 128  # or 64
```

### Slow Training

- Ensure images are properly sized (32×32)
- Check if OpenCV is using optimized builds
- Consider reducing dataset size for testing

### Poor Accuracy

For Dataset 2 (97 classes), low accuracy (~5%) is expected due to:
- Limited model capacity (only 128 features)
- High number of classes
- Pure Python constraints

To improve:
- Increase `NUM_FILTERS` to 8-12
- Add more dense layer neurons
- Train for more epochs (if time permits)

## Complexity Analysis

### Dataset 1 (10 classes)

```
Parameters: 1,328
MACs: 9,728
FLOPs: 19,456
Training time: 29 min
Test accuracy: 72.88%
```

### Dataset 2 (97 classes)

```
Parameters: 12,551
MACs: 20,864
FLOPs: 41,728
Training time: 29.7 min
Test accuracy: 5.48%
```

## Citation

If you use this code for academic purposes, please cite:

```bibtex
@misc{gnr638_assignment01,
  title={Custom Deep Learning Framework for Image Classification},
  author={Your Name},
  year={2026},
  institution={IIT Bombay},
  course={GNR638: Machine Learning for Remote Sensing II}
}
```

## References

1. Howard, A. G., et al. (2017). MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications.
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
3. CS231n: Convolutional Neural Networks for Visual Recognition - Stanford University
