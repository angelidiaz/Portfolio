# Sentiment Analysis using Machine Learning

## Overview
This project implements a machine learning-based approach to sentiment analysis using bag-of-words text representation. The system analyzes Amazon product reviews to classify them as expressing either positive or negative sentiments.

Two classical models are applied:
- **Perceptron**
- **Logistic Regression**

These models are trained using both **binary** and **count-based** bag-of-words representations. To optimize performance, we apply **grid search** and **5-fold cross-validation**.

---

## Project Structure

### 1. **Data Preprocessing** (`preprocessing_data.py`)
- Loads TSV-formatted labeled datasets
- Text cleaning and tokenization
- Feature extraction using the bag-of-words model
- Support for both:
  - **Binary features** (word presence)
  - **Count features** (word frequency)
- Train/test split

### 2. **Model Training and Evaluation** (`sentiment_analysis.py`)
- Implements:
  - Perceptron classifier
  - Logistic Regression classifier
- Model training and testing
- Hyperparameter tuning using grid search
- Evaluation using training/test accuracy

---

## Features

### Text Processing
- Handles punctuation and digits
- Case normalization (lowercasing)
- Vocabulary building from training data
- Feature matrix generation based on BoW

### Model Optimization
- Grid search to tune hyperparameters
- 5-fold cross-validation for robustness
- Accuracy metrics for both training and test datasets

---

## Dataset
- **Format:** TSV (Tab-separated values)
- **Files:**
  - `reviews_train.tsv`: Training dataset
  - `reviews_test.tsv`: Testing dataset
- **Labels:**
  - `+1` for positive sentiment
  - `-1` for negative sentiment

Each entry contains the review text and its associated sentiment label.

---

## Dependencies
- **NumPy**: Numerical operations and matrix handling
- **Pandas**: Data analysis (optional depending on further extensions)
- **Scikit-learn**: Model implementation, grid search, and evaluation
- **CSV**: Reading TSV files

---

## Usage
The project supports the following workflows:
1. Preprocessing and vectorizing review data using binary or count BoW.
2. Training classifiers (Perceptron or Logistic Regression) on preprocessed data.
3. Evaluating classifier performance using cross-validation.
4. Comparing the effects of binary vs. count feature representation.
5. Identifying significant words contributing to sentiment classification.
