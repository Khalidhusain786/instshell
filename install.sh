#!/bin/bash

# Repository name
REPO_NAME="instshell"
REPO_URL="https://github.com/Khalidhusain786/instshell.git"

echo "Updating and cleaning up..."
cd /home/kali
rm -rf $REPO_NAME

echo "Cloning repository..."
git clone $REPO_URL

if [ -d "$REPO_NAME" ]; then
    cd $REPO_NAME
    echo "Setting permissions..."
    chmod +x *
    
    echo "Installing requirements..."
    # Kali Linux ke liye --break-system-packages zaroori hai
    pip install selenium undetected-chromedriver webdriver-manager --break-system-packages
    
    echo "Running the tool..."
    python3 inst.py
else
    echo "Error: Directory not found. Check your GitHub link."
fi
