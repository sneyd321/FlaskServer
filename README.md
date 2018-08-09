This repository contains a python based server used by the AndroidDemo Project

This project uses jupyter notebook files to iterate through a CSV as well as contains model files for object detection

Setting up the server environment
This guide will follow the tutorial used here (https://www.tensorflow.org/install/install_windows)

Required:
Anaconda 
Cuda compatible GPU (https://developer.nvidia.com/cuda-gpus)
Nvidia account (Free)
Git bash (optional)


Step 1 - Verify software
Verify that GPU is compatible with this software. Go to https://developer.nvidia.com/cuda-gpus to check compatibility of 3.0 or higher. If your GPU is not compatible then stop this tutorial and get a better PC.

Step 2 - Get Toolkit
Go to https://developer.nvidia.com/cuda-downloads
Click legacy releases (If you get the most recent version everything will break at the last step...Trust me)
Click on CUDA Toolkit 9.0 (Sept 2017) 
This tutorial will download OS: Windows, Architecture: x86_64, Version: 10, Installer Type: Local
Download “Base Installer”
Follow on screen instruction

Step 3 - Download cuDNN
Go to https://developer.nvidia.com/cudnn
Select Download cuDNN
Get an account or sign in
Agree to user agreement
Download cuDNN for CUDA 9.0 
Then select for Windows 10
Follow on screen instructions

Step 4 - Copy and Paste
Open two instances on the File Explorer
In the first instance navigate to C:/Program Files/NVIDIA GPU Computing Toolkit/v9.0
In the second instance navigate to the cuDNN zip
Extract folder and copy and paste the the files in the bin, include and lib folders into their respective folders in the C:/Program Files/NVIDIA GPU Computing Toolkit/v9.0

Step 5 - Get Anaconda Prompt
Go to https://www.anaconda.com/download/#windows
Install latest version of Python 3
Follow on screen instructions

Step 6 - Create Conda environment (anaconda is just a python environment, you know anaconda is a snake, python is a snake)
Run “conda create -n tensorflow pip python=3.5”
Run “activate tensorflow”
Verify pip is installed by running “conda install pip”
Run “pip install --ignore-installed --upgrade tensorflow-gpu”
Verify installation by typing “python” then “import tensorflow as tf.
If there are no errors tensorflow setup is complete
If there are errors check “Common installation problems” at https://www.tensorflow.org/install/install_windows 


Step 7 - Getting Jupyter notebook (IDE for the server)
Run “conda install jupyter”
Run “jupyter-notebook” in the folder that contains all server files

Step 8 - Getting the rest of the libraries
Run  “conda install flask”
Download package or git clone https://github.com/keras-team/keras.git
Go back to anaconda prompt and go to the keras library
Run “python setup.py install”
Run “conda install matplotlib”
Run “conda install -c anaconda opencv”
Run “conda install -c anaconda pillow”


Step 8 - Running the server
Go to command prompt and type ipconfig
Go to “Wireless LAN adapter Wi-Fi” and get IPv4 Address
Go to anaconda prompt and type jupyter-notebook
Click on server.py
Scroll down to line 126 and change the ip to whatever ipconfig said
Close jupyter-notebook 
In anaconda prompt type “python server.py”
