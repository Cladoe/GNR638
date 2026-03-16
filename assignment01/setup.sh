#!/bin/bash

# GNR638 Assignment 1 - Setup Script
# This script initializes the project for first use

echo "======================================================================"
echo "GNR638 Assignment 1 - Project Setup"
echo "======================================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3 first"
    exit 1
fi

echo "✅ Python 3 found"

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "❌ Error: pip is not installed"
    echo "Please install pip first"
    exit 1
fi

echo "✅ pip found"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Error installing dependencies"
    exit 1
fi

# Create data directory structure
echo ""
echo "Creating data directory structure..."
mkdir -p data/dataset1/{train,test}
mkdir -p data/dataset2/{train,test}
echo "✅ Data directories created"

echo ""
echo "======================================================================"
echo "Setup Complete! 🎉"
echo "======================================================================"
echo ""
echo "Next steps:"
echo "  1. Copy your datasets to data/dataset1/ and data/dataset2/"
echo "  2. Update paths in config.py if needed"
echo "  3. Run: jupyter notebook assignment01_final_codes.ipynb"
echo ""
echo "For more information:"
echo "  • Quick start: See QUICK_REFERENCE.md"
echo "  • Full guide: See USAGE.md"
echo "  • GitHub setup: See GITHUB_SETUP.md"
echo ""
echo "======================================================================"
