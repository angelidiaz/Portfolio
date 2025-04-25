# MNIST Digit Classification Project

## Overview
This project implements and compares multiple approaches to classify handwritten digits from the MNIST dataset. It demonstrates a progression from traditional machine learning techniques to a deep learning-based Convolutional Neural Network (CNN).

Two categories of models are applied:
- **Traditional ML classifiers** (SVM and Logistic Regression)
- **Deep Learning with CNN (PyTorch)**

These models are trained and evaluated using comprehensive accuracy metrics.

---

## Project Structure

### 1. **Data Preprocessing and Utilities** (`preprocessing_data.py`)
- Loads and preprocesses the MNIST dataset
- Visualization functions for inspection
- Splits dataset into training and test sets

### 2. **Traditional ML Models** (`mnist_classification_part1.ipynb`)
- Implements classical classification methods:
  - Linear Support Vector Classifier (LinearSVC)
  - Logistic Regression (Multinomial and One-vs-Rest)
- Optional dimensionality reduction using PCA
- Hyperparameter tuning via grid search
- Evaluation using classification accuracy

### 3. **Deep Learning with CNN** (`mnist_classification_part2.ipynb`)
- Constructs a CNN model using PyTorch
- Includes:
  - Convolutional layers with ReLU
  - Max pooling layers
  - Dropout for regularization
  - Fully connected layers
- Implements training and validation loops
- Final evaluation on test data

---

## Features

### Data Processing
- Based on the MNIST dataset:
  - 60,000 training samples
  - 10,000 test samples
- Images: 28×28 grayscale pixels
- Labels: 10 digit classes (0 through 9)
- Converts image data to:
  - Flat feature vectors for ML models
  - 4D tensors `(batch_size, 1, 28, 28)` for CNN (Batch size refers to the number of training samples the model processes before updating its weights)

### Traditional ML Models
- **Linear SVC**:
  - One-vs-Rest strategy
  - Squared hinge loss
  - Grid search for optimal regularization
- **Logistic Regression**:
  - Multinomial softmax classifier
  - One-vs-Rest strategy
  - L-BFGS solver for optimization
- **PCA**:
  - Optional reduction of input dimensions

### CNN Architecture
- Two convolutional layers:
  - Conv2D(1→32, 3×3) → ReLU → MaxPool(2×2)
  - Conv2D(32→64, 3×3) → ReLU → MaxPool(2×2)
- Flatten layer for dense input
- Fully connected layers:
  - Linear(1600→128) → Dropout(0.5)
  - Linear(128→10)

---

## Dataset
- **Source**: MNIST handwritten digit dataset
- **Format**:
  - Input: 28×28 grayscale images
  - Output: Digit labels from 0 to 9


---

## Dependencies
- **PyTorch**: Deep learning framework
- **NumPy**: Array and matrix operations
- **Scikit-learn**: ML models and preprocessing
- **Matplotlib**: Data visualization
- **Pandas**: Data manipulation

---

## Usage

The project supports the following workflows:
1. Load and preprocess the MNIST dataset.
2. Train ML classifiers (LinearSVC, Logistic Regression) with or without PCA.
3. Train and validate the CNN model using PyTorch.
4. Evaluate performance across all models using test accuracy.

