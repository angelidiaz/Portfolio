# Netflix Matrix Completion Project

## Overview
This project implements matrix completion techniques for predicting missing user ratings in a movie recommendation setting. The input is a sparse user-movie matrix derived from a Netflix-like dataset.

Two complementary approaches are applied:
- **Expectation-Maximization (EM) with Gaussian Mixture Models (GMMs)**
- **Alternating Least Squares (ALS)**

Both methods are evaluated based on prediction performance and model complexity.

---

## Project Structure

### 1. **Matrix Completion and Analysis** (`matrix_completion.ipynb`)
- Loads the incomplete and ground-truth rating matrices
- Implements EM and ALS-based completion methods
- Computes model evaluation metrics:
  - Log-likelihood
  - BIC (Bayesian Information Criterion)
  - RMSE (Root Mean Squared Error)
- Compares predictive accuracy across models and different hyperparameters

### 2. **Utility Functions** (`utils.py`)
- Core support functions for EM with GMMs
- Implements:
  - GMM initialization
  - Log-likelihood and BIC calculations
  - RMSE computation
---

## Techniques

### Expectation-Maximization with GMM
- Models users as samples from a mixture of Gaussian distributions
- Handles missing ratings by marginalizing over unobserved entries
- Iteratively applies:
  - **E-Step**: Calculates posterior responsibilities
  - **M-Step**: Updates parameters (means, variances, mixing weights)

### Alternating Least Squares (ALS)
- Matrix factorization technique for collaborative filtering
- Decomposes the rating matrix into user and item latent features
- Alternates optimization using ridge regression


---

## Dataset
- **Format:** Text file
- **Files:**
  - `netflix_incomplete.txt`: Sparse matrix with unknown ratings
  - `netflix_complete.txt`: Complete ratings for evaluation
- **Structure:**
  - Rows represent users
  - Columns represent movies
  - Some entries are missing in the incomplete version

---

## Dependencies
- **NumPy**: Matrix and array computations
- **SciPy**: Statistical functions and optimization
- **Matplotlib**: Visualization of model outputs
- **Pandas**: Data handling and analysis
- `typing.NamedTuple`: For structured GMM representation

---

## Usage
The project supports the following workflow:
1. Load and inspect the sparse and complete rating matrices.
2. Run EM with GMM or ALS to complete the matrix.
3. Tune hyperparameters such as the number of Gaussian components (K).
4. Evaluate models using log-likelihood, BIC, and RMSE.
---

