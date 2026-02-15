"""
Configuration file for GNR638 Assignment 1
"""

# Data paths
DATA_PATH_1 = './data/dataset1/'  # Update with your dataset 1 path
DATA_PATH_2 = './data/dataset2/'  # Update with your dataset 2 path

# Training hyperparameters
EPOCHS = 2
BATCH_SIZE = 256
LEARNING_RATE = 0.08

# Model architecture
NUM_FILTERS = 4  # Number of filters in conv layer
IMAGE_SIZE = 32  # Input image size
POOL_SIZE = 2    # Pooling kernel size

# Training constraints
MAX_TRAIN_TIME_HOURS = 3
MAX_EVAL_TIME_HOURS = 1

# Gradient clipping
GRAD_CLIP = 10.0

# Random seed for reproducibility
RANDOM_SEED = 42
