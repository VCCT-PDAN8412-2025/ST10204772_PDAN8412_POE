# PDAN8412 POE Part 3

## Project Description
This project implements a Convolutional Neural Network (CNN) for recognising and decoding characters from CAPTCHA images. The main goal is to develop a robust machine learning model capable of accurately transcribing the text displayed in CAPTCHA images. The project is built using Python and the TensorFlow/Keras. The Jupyter Notebook included in this repository manages the entire workflow from data loading and preprocessing to model definition, training, and evaluation.

## Files in this Repository
- **Allana Morris_ST10204774_PDAN8412_POE Part 3.ipynb** - The main notebook containing all code for data exploration, preprocessing including augmentation, CNN model construction, training, and evaluation.
- **Dataset Installation Verification Script.py** - A helper script used to verify that the dataset folder is correctly placed within the project directory. 
- **README.md** - This markdown file containing the instruction for setting up


## Prerequisites
To run this project, ensure you have:

- Python (3.10.11 recommended)
- Jupyter Notebook or JupyterLab
- The **1M_Big_Captcha_Dataset** folder (installation intructions to follow)

## Installation

### 1. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
.\venv\Scripts\activate 
```

### 2. Install Required Packages
Install all libraries required to execute the notebook:
```bash
%pip install --upgrade pip setuptools wheel
%pip install -r requirements.txt
```
or
```bash
conda install -c conda-forge tensorflow numpy pandas matplotlib seaborn pillow scikit-learn tqdm editdistance pyspark keras glob
```

## Dataset Setup
The project requires a dataset folder named exactly: **1M_Big_Captcha_Dataset**

### 1. Acquire the Dataset

**Dataset Onedrive Link:** [Dataset OneDrive Folder](https://advtechonline-my.sharepoint.com/:f:/g/personal/st10204772_vcconnect_edu_za/IgCZ5bCXuRigRrgs4mNaeBcFAd4aw2KVIZfDxlmBo4CNgKw?e=Q3DNsh)

#### Dataset Download Instructions

1. **Open the link** to the dataset.  
2. **Select "Download"** to download the ZIP file.  
3. **Locate the downloaded ZIP file**, usually found in your `Downloads` folder.  
4. **Extract the ZIP folder** to the same directory where your Jupyter Notebook file (`.ipynb`) is located.


### 2. Folder Structure
Your project directory should look like this:
```mermaid
.
├── Allana Morris_ST10204774_PDAN8412_POE Part 3.ipynb
├── Dataset Installation Verification Script.py
└── 1M_Big_Captcha_Dataset/
    ├── XXXXX.png
    ├── YYYYY.png
    └── ...
```

### 3. Verify Installation
Run the verification script to confirm the dataset is correctly installed:
```bash
python "Dataset Installation Verification Script.py"
```
If the dataset is set up correctly, the script will output the first few filenames.

## Usage

### 1. Start Jupyter
```bash
jupyter notebook
```
or
```bash
jupyter lab
```

### 2. Open the Notebook
Open:
**Allana Morris_ST10204774_PDAN8412_POE Part 3.ipynb**

### 3. Execute the Notebook
Run all cells sequentially from top to bottom. The notebook includes:
- Package imports and environment configuration
- Data loading and initial exploration
- Data preprocessing and augmentation
- CNN model construction using Keras
- Model training
- Evaluation of model performance and visualisation of results

### Due to GitHub's upload size rescrictions, the `best_model.keras` file will only be available on ARC