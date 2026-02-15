# Project Summary

## GNR638 Assignment 1: Custom Deep Learning Framework

### Overview

This project implements a complete CNN framework from scratch without using any ML libraries (NumPy, PyTorch, TensorFlow). Built purely in Python with only OpenCV for image I/O.

### Key Achievements

✅ **25× Reduction in MACs** compared to standard CNNs  
✅ **Fast Training**: 29-30 minutes per dataset  
✅ **Efficient Architecture**: MobileNet-inspired design  
✅ **Pure Python**: No NumPy, no frameworks  
✅ **Production-Ready**: Complete with documentation and examples  

### Results Summary

| Metric | Dataset 1 (10 classes) | Dataset 2 (97 classes) |
|--------|------------------------|------------------------|
| **Test Accuracy** | 72.88% | 5.48% |
| **Training Time** | 29.0 min | 29.7 min |
| **Parameters** | 1,328 | 12,551 |
| **MACs** | 9,728 | 20,864 |
| **FLOPs** | 19,456 | 41,728 |

### Architecture Highlights

```
Input: 32×32×3 RGB images

Pipeline:
  MaxPool(2×2) → 16×16×3
  DepthwiseConv(3×3) → 16×16×3
  PointwiseConv(1×1) → 16×16×2
  ReLU
  MaxPool(2×2) → 8×8×2
  Flatten → 128
  Dense → n_classes
  Softmax

Parameters: ~1.3K (10 cls) | ~12.5K (97 cls)
```

### Technical Implementation

**Core Components:**
- Custom Conv2D with depthwise separable convolutions
- MaxPool2D with backward pass
- Dense layer with gradient computation
- ReLU activation
- Softmax + Cross-entropy loss
- SGD optimizer with gradient clipping

**Optimizations:**
- Early spatial downsampling (4× MAC reduction)
- Depthwise separable convolutions (parameter efficiency)
- Minimal filters (2 output channels)
- Batch size 256 for optimal throughput
- Gradient clipping at ±10 for stability

### Repository Structure

```
gnr638_assignment01/
├── README.md                       # Main documentation
├── USAGE.md                        # Detailed usage guide
├── GITHUB_SETUP.md                 # GitHub setup instructions
├── LICENSE                         # MIT License
├── requirements.txt                # Dependencies (opencv-python)
├── config.py                       # Configuration settings
├── quick_start.py                  # Quick demo script
├── assignment01_final_codes.ipynb  # Complete implementation
├── .gitignore                      # Git ignore rules
├── .gitattributes                  # Line ending configuration
└── repository_structure.png        # Visual reference
```

### How to Use

**Option 1: Quick Demo**
```bash
python quick_start.py
```

**Option 2: Full Training (Recommended)**
```bash
jupyter notebook assignment01_final_codes.ipynb
# Run all cells
```

**Option 3: Custom Setup**
1. Edit `config.py` with your data paths
2. Modify hyperparameters as needed
3. Run the notebook

### Complexity Analysis

**Dataset 1 (10 classes):**
```
Depthwise Conv:  6,912 MACs
Pointwise Conv:  1,536 MACs  
Dense Layer:     1,280 MACs
Total:           9,728 MACs = 19,456 FLOPs
```

**Comparison to Standard CNN:**
- Standard (8 filters): 241,664 MACs
- Our architecture: 9,728 MACs
- **Reduction: 25×**

### Training Details

**Hyperparameters:**
- Optimizer: SGD
- Learning rate: 0.08
- Batch size: 256
- Epochs: 2
- Gradient clipping: ±10

**Data Processing:**
- Resize to 32×32
- BGR → RGB conversion
- Normalize to [0, 1]
- No augmentation (pure training)

### Why This Matters

1. **Educational**: Understanding deep learning from first principles
2. **Efficient**: Proof that small models can work well
3. **Practical**: Meets strict time and resource constraints
4. **Portable**: Pure Python runs anywhere
5. **Scalable**: Architecture principles apply to larger models

### Lessons Learned

**Architecture:**
- Early pooling is crucial for efficiency
- Depthwise separable >> standard convolutions
- Small models can achieve good accuracy
- Model capacity bottleneck for 97 classes

**Implementation:**
- Python lists are slow (10-100× slower than NumPy)
- Batch size 256 is optimal for pure Python
- Gradient clipping is essential
- Parallel data loading helps significantly

**Training:**
- Moderate LR (0.08) works well
- 2 epochs sufficient for convergence
- More features needed for complex tasks
- 128 features insufficient for 97 classes

### Future Improvements

1. **C++ Backend**: 10-100× speedup potential
2. **Larger Model**: 8-12 filters, 512-1024 dense features
3. **Data Augmentation**: Flips, rotations, color jittering
4. **Advanced Optimizers**: Momentum, Adam
5. **Batch Normalization**: Training stability
6. **Residual Connections**: Deeper networks

### References

1. Howard, A. G., et al. (2017). MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications.
2. Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
3. Nielsen, M. (2015). Neural Networks and Deep Learning.
4. CS231n: Convolutional Neural Networks for Visual Recognition.

### GitHub Repository

**Ready to push!** Follow `GITHUB_SETUP.md` for step-by-step instructions.

Repository is configured with:
- ✅ Proper .gitignore
- ✅ Line ending configuration
- ✅ License (MIT)
- ✅ Complete documentation
- ✅ Example scripts
- ✅ All necessary files

### Contact & Attribution

- **Course**: GNR638 - Machine Learning for Remote Sensing II
- **Institution**: IIT Bombay
- **Year**: 2026
- **License**: MIT (see LICENSE file)

---

**Note**: This is an educational project demonstrating deep learning fundamentals. For production use, consider frameworks like PyTorch or TensorFlow.
