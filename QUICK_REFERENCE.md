# Quick Reference Guide

## 📁 File Overview

| File | Purpose |
|------|---------|
| `README.md` | Main documentation (GitHub front page) |
| `USAGE.md` | Detailed usage instructions |
| `GITHUB_SETUP.md` | Step-by-step GitHub setup |
| `PROJECT_SUMMARY.md` | Complete project overview |
| `assignment01_final_codes.ipynb` | **Main code - RUN THIS** |
| `config.py` | Configuration settings |
| `quick_start.py` | Quick demo script |
| `requirements.txt` | Dependencies |
| `.gitignore` | Git ignore rules |
| `.gitattributes` | Line ending config |
| `LICENSE` | MIT License |

## 🚀 Quick Start (3 Steps)

1. **Install**:
   ```bash
   pip install opencv-python
   ```

2. **Configure**: Edit `config.py` with your data paths

3. **Run**: Open `assignment01_final_codes.ipynb` and run all cells

## 📊 Expected Results

### Dataset 1 (10 classes)
- ⏱️ Training: 29 min
- 🎯 Accuracy: 72.88%
- 📦 Parameters: 1,328

### Dataset 2 (97 classes)
- ⏱️ Training: 29.7 min
- 🎯 Accuracy: 5.48%
- 📦 Parameters: 12,551

## 🔧 Configuration (config.py)

```python
# Must change these:
DATA_PATH_1 = './data/dataset1/'  # Your dataset 1 path
DATA_PATH_2 = './data/dataset2/'  # Your dataset 2 path

# Can tune these:
LEARNING_RATE = 0.08
BATCH_SIZE = 256
EPOCHS = 2
NUM_FILTERS = 4
```

## 🐙 GitHub Setup (5 Steps)

```bash
cd gnr638_assignment01
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

See `GITHUB_SETUP.md` for detailed instructions.

## 🏗️ Architecture

```
Input (32×32×3)
    ↓
MaxPool → 16×16×3
    ↓
DepthwiseConv → 16×16×3
    ↓
PointwiseConv → 16×16×2
    ↓
ReLU
    ↓
MaxPool → 8×8×2
    ↓
Flatten → 128
    ↓
Dense → Softmax → Classes
```

## 💡 Key Features

✨ **25× fewer MACs** than standard CNN  
✨ **Pure Python** (no NumPy/PyTorch)  
✨ **Fast training** (~30 min)  
✨ **MobileNet-inspired** architecture  

## 🔥 Troubleshooting

### Out of Memory
```python
BATCH_SIZE = 128  # or 64
```

### Slow Training
- Check image size (should be 32×32)
- Verify OpenCV installation
- Reduce dataset for testing

### Low Accuracy (Dataset 2)
Expected! Only 128 features for 97 classes.

To improve:
- Increase `NUM_FILTERS` to 8-12
- Add more dense neurons
- Train longer (if time permits)

## 📚 Documentation Map

**New to project?** → Start with `README.md`

**Ready to train?** → Follow `USAGE.md`

**Setting up GitHub?** → Check `GITHUB_SETUP.md`

**Want overview?** → Read `PROJECT_SUMMARY.md`

**Quick test?** → Run `quick_start.py`

**Full training?** → Open `assignment01_final_codes.ipynb`

## 🎯 Assignment Requirements

| Requirement | Status |
|-------------|--------|
| No NumPy/PyTorch | ✅ Pure Python |
| Train < 3 hours | ✅ ~30 min |
| Eval < 1 hour | ✅ ~10 min |
| Backpropagation | ✅ Implemented |
| Two datasets | ✅ Both tested |

## 📞 Need Help?

1. Check `USAGE.md` for detailed instructions
2. See `GITHUB_SETUP.md` for Git issues
3. Review `PROJECT_SUMMARY.md` for technical details
4. Look at `config.py` for settings

## 🏆 Results Summary

| Metric | Dataset 1 | Dataset 2 |
|--------|-----------|-----------|
| Classes | 10 | 97 |
| Accuracy | 72.88% | 5.48% |
| Time | 29.0 min | 29.7 min |
| MACs | 9,728 | 20,864 |
| Params | 1,328 | 12,551 |

## ✅ Pre-Push Checklist

Before pushing to GitHub:

- [ ] Updated `config.py` paths
- [ ] Tested notebook runs completely
- [ ] Removed any personal/sensitive data
- [ ] Verified .gitignore excludes data files
- [ ] Read `GITHUB_SETUP.md`
- [ ] Created GitHub repository
- [ ] Ready to push!

## 📝 Citation

```bibtex
@misc{gnr638_assignment01,
  title={Custom Deep Learning Framework},
  author={Your Name},
  year={2026},
  institution={IIT Bombay}
}
```

---

**Everything you need is in this directory. Happy coding! 🚀**
