#!/bin/bash

# Update all installed packages
sudo yum update -y

# Check if Python 3 is installed, and install if not
if ! command -v python3 &> /dev/null
then
    echo "Python 3 not found, installing..."
    sudo yum install python3 -y
else
    echo "Python 3 is already installed."
fi

# Check if pip is installed, and install if not
if ! command -v pip3 &> /dev/null
then
    echo "pip3 not found, installing..."
    sudo yum install python3-pip -y
else
    echo "pip3 is already installed."
fi

# Check if TensorFlow is installed, and install if not
if ! python3 -c "import tensorflow" &> /dev/null
then
    echo "TensorFlow not found, installing..."
    sudo pip3 install tensorflow
else
    echo "TensorFlow is already installed."
fi

# Check if Streamlit is installed, and install if not
if ! python3 -c "import streamlit" &> /dev/null
then
    echo "Streamlit not found, installing..."
    sudo pip3 install streamlit
else
    echo "Streamlit is already installed."
fi

# Check if Pillow is installed, and install if not
if ! python3 -c "from PIL import Image" &> /dev/null
then
    echo "Pillow not found, installing..."
    sudo pip3 install pillow
else
    echo "Pillow is already installed."
fi

# Check if NumPy is installed, and install if not
if ! python3 -c "import numpy" &> /dev/null
then
    echo "NumPy not found, installing..."
    sudo pip3 install numpy
else
    echo "NumPy is already installed."
fi
