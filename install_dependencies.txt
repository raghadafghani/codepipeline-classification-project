#!/bin/bash

# Update all installed packages
sudo yum update -y

# Install Python 3 (if not already installed)
sudo yum install python3 -y

# Install pip for Python 3 (if not already installed)
sudo yum install python3-pip -y

# Install required Python libraries for TensorFlow, Streamlit, etc.
pip3 install --upgrade pip  # Upgrade pip to the latest version
pip3 install streamlit tensorflow pillow numpy  # Install required libraries

# Optional: Ensure Streamlit is installed and check version
streamlit --version
