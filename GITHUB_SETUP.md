# GitHub Setup Guide

## Step 1: Initialize Git Repository

Open terminal in the project directory and run:

```bash
cd gnr638_assignment01
git init
```

## Step 2: Add Files

```bash
git add .
```

## Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: GNR638 Assignment 1 - Custom CNN Framework"
```

## Step 4: Create GitHub Repository

1. Go to [github.com](https://github.com) and login
2. Click the "+" icon in top right → "New repository"
3. Name it: `gnr638-assignment01` (or your preferred name)
4. **Don't** initialize with README (we already have one)
5. Click "Create repository"

## Step 5: Connect Local to Remote

Copy the commands from GitHub (they look like this):

```bash
git remote add origin https://github.com/YOUR_USERNAME/gnr638-assignment01.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Step 6: Verify

Go to your GitHub repository URL to verify all files are uploaded.

## Optional: Add Topics/Tags

On GitHub, click the gear icon next to "About" and add topics:
- `deep-learning`
- `convolutional-neural-networks`
- `pure-python`
- `image-classification`
- `mobilenet`
- `iit-bombay`

## Updating Repository Later

When you make changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

## .gitignore Already Configured

The `.gitignore` file is already set up to exclude:
- Data directories
- Model weights
- Temporary files
- IDE configurations
- Python cache files

This keeps your repository clean and lightweight.

## Repository Structure

Your GitHub repo will look like this:

```
gnr638-assignment01/
├── README.md                       ← GitHub front page
├── USAGE.md                        ← Detailed usage guide
├── LICENSE                         ← MIT License
├── requirements.txt                ← Dependencies
├── config.py                       ← Configuration
├── quick_start.py                  ← Quick demo
├── assignment01_final_codes.ipynb  ← Main notebook
├── .gitignore                      ← Git ignore rules
└── .gitattributes                  ← Line ending rules
```

## Making Repository Public/Private

- **Public**: Anyone can see it (good for portfolio)
- **Private**: Only you and invited collaborators can see it

To change: Go to Settings → Danger Zone → Change visibility

## Best Practices

1. **Write good commit messages**: Describe what changed and why
2. **Commit frequently**: Small, logical commits are better
3. **Don't commit large data files**: Use `.gitignore`
4. **Update README**: Keep it current with any changes
5. **Add LICENSE**: Always include (MIT is already added)

## Troubleshooting

### Authentication Error

If you get authentication errors, use a Personal Access Token:

1. GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select `repo` scope
4. Use token as password when prompted

### Large File Error

If files are too large (>100MB), use Git LFS or exclude them:

```bash
git rm --cached large_file.pkl
echo "large_file.pkl" >> .gitignore
git add .gitignore
git commit -m "Exclude large files"
```

## Need Help?

- GitHub Docs: https://docs.github.com/
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
