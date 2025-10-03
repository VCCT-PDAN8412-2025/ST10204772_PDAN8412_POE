# PDAN8412POE – Part One

## Project Overview
This repository contains the work for **Part One** of the PDAN8412 Portfolio of Evidence (POE). The task involves building and evaluating a **Long Short-Term Memory (LSTM)** neural network for text classification using the **Spooky Author Identification dataset**.

The main objectives of this part are:  
1. To prepare and clean the dataset for deep learning.  
2. To perform **exploratory data analysis (EDA)** with visualisations of author styles and text features.  
3. To design, train, and evaluate an **LSTM model** for author classification.

---

## Dataset
The dataset is the **Spooky Author Identification dataset** (Kaggle). It contains ~20,000 short excerpts from works by:  
- Edgar Allan Poe (EAP)  
- H. P. Lovecraft (HPL)  
- Mary Wollstonecraft Shelley (MWS)  

Each excerpt is labeled with its corresponding author.

---

## Analysis Conducted

### 1. Data Cleaning & Preparation
- Removal of duplicates and handling of missing values.  
- Tokenisation and sequence padding to prepare inputs for the LSTM.  
- Transformation into numerical representations suitable for deep learning.

### 2. Exploratory Data Analysis (EDA)
Visualisations were produced to highlight dataset characteristics:  
- Distribution of excerpts by author.  
- Token length distributions overall and by author.  
- Word cloud of the most frequent terms.  
- Stylistic feature comparisons (average sentence length, punctuation counts, type-token ratio).  
- TF-IDF feature importance for the top terms.

### 3. LSTM Model Design & Training
- The LSTM model was implemented using TensorFlow/Keras.  
- Input: padded sequences of tokenised text.  
- Layers: Embedding layer, LSTM layers, Dense output layer with softmax activation.  
- Training used categorical cross-entropy loss and the Adam optimizer.  
- Early stopping was applied with patience to prevent overfitting.

---

## Results
- The LSTM model achieved **progressive improvement over epochs**, with training accuracy increasing and validation accuracy stabilising.  
- The validation accuracy demonstrated that the model could generalise to unseen data.  
- Some divergence between training and validation suggested areas for fine-tuning, but overall performance confirmed the suitability of LSTMs for this classification task.

---

## How to Run
1. Clone this repository.  
2. Ensure Python 3.x and the following libraries are installed:  
   - `pandas`  
   - `numpy`  
   - `matplotlib`  
   - `seaborn`  
   - `tensorflow` / `keras`  
   - `scikit-learn`  
3. Open the Jupyter Notebook (`PDAN8412_POE.ipynb`).  
4. Run all cells sequentially to reproduce results.

---

## File Structure
- `PDAN8412_POE.ipynb` – Jupyter Notebook with code and analysis.  
- `SpookyAuthor.csv` – Dataset used for training and testing.  
- `README.md` – Project overview (this file).

---

## Conclusion
Part One demonstrates the process of preparing a literary dataset, performing detailed exploratory analysis, and implementing an **LSTM model for author classification**. The results highlight the model’s ability to learn distinct stylistic and lexical patterns of different authors, forming a foundation for more advanced experiments in later parts of the POE.
