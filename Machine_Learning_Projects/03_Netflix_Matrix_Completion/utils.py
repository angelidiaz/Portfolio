"""
Gaussian Mixture Model (GMM) Implementation and Utilities

This module provides a comprehensive implementation of Gaussian Mixture Models and related
utility functions for model initialization, evaluation, and selection. The implementation
supports multivariate Gaussian distributions with diagonal covariance matrices.
"""

from typing import NamedTuple, Tuple
import numpy as np


class GaussianMixture(NamedTuple):
    """
    A named tuple representing a Gaussian Mixture Model (GMM) with K components.

    This class represents a mixture of K Gaussian distributions, each defined by its
    mean (μ), variance (σ²), and mixing coefficient (p). The mixture model is
    defined as:

    P(x) = Σ(k=1 to K) p_k * N(x | μ_k, σ²_k)

    where N(x | μ, σ²) is the normal distribution.

    Attributes:
        mu (np.ndarray): Mean vectors for each Gaussian component.
                        Shape: (K, d) where:
                        - K is the number of components
                        - d is the dimension of the feature space
                        Each row k represents the mean vector μ_k

        var (np.ndarray): Variances for each Gaussian component.
                          Shape: (K,) where:
                          - K is the number of components
                          Each element k represents the variance σ²_k

        p (np.ndarray): Mixing coefficients (weights) for each component.
                           Shape: (K,) where:
                           - K is the number of components
                           Each element k represents the weight p_k
                           Must satisfy: Σp_k = 1 and all p_k ≥ 0
        """

    mu: np.ndarray
    var: np.ndarray
    p: np.ndarray


def init(X: np.ndarray, K: int,
         seed: int = 0) -> Tuple[GaussianMixture, np.ndarray]:
    """
    Initializes a Gaussian Mixture Model (GMM) with K components using random initialization.

    This function performs the following initialization steps:
    1. Sets random seed for reproducibility
    2. Initializes mixing coefficients with uniform weights (1/K)
    3. Randomly selects K data points as the initial component means
    4. Computes initial variances based on mean squared distances
    5. Creates uniform initial posterior probabilities

    Args:
        X: Data array of shape (n, d) where:
           - n is the number of samples
           - d is the number of features
        K: Number of Gaussian components in the mixture
        seed: Random seed for reproducibility (default: 0)

    Returns:
        tuple: Contains:
            - mixture (GaussianMixture): Initialized GMM with attributes:
                * mu: (K, d) array of component means
                * var: (K,) array of component variances
                * p: (K,) array of mixing coefficients
            - post: (n, K) array of posterior probabilities where:
                * Each row sums to 1
                * Initially set to uniform values (1/K)

    Note:
        - Variances are computed using mean squared distances from each point
          to the corresponding component mean
        - All random selections are controlled by the seed parameter for
          reproducibility
    """

    # Set random seed for reproducibility
    np.random.seed(seed)

    # Get number of samples
    n, _ = X.shape

    # Initialize mixing coefficients uniformly
    p = np.ones(K) / K

    # Randomly select K points as initial means
    mu = X[np.random.choice(n, K, replace=False)]

    # Initialize and compute variances
    var = np.zeros(K)

    # Compute mean squared distance to jth component mean
    for j in range(K):
        var[j] = ((X - mu[j])**2).mean()

    # Create GMM with initialized parameters
    mixture = GaussianMixture(mu, var, p)

    # Initialize posterior probabilities uniformly
    post = np.ones((n, K)) / K

    return mixture, post

def rmse(X, Y):
    """
    Calculate the Root Mean Square Error (RMSE) between two arrays.

    RMSE measures the average magnitude of prediction errors, giving a single
    value that represents the typical deviation between predicted and actual values.
    The formula used is: RMSE = √(mean((X - Y)²))

    Args:
        X (np.ndarray): First array (typically predictions or estimates)
        Y (np.ndarray): Second array (typically true or reference values)
                        Must have the same shape as X

    Returns:
        float: The RMSE value between X and Y

        Raises:
            ValueError: If X and Y have different shapes
    """

    return np.sqrt(np.mean((X - Y)**2))

def bic(X: np.ndarray, mixture: GaussianMixture,
        log_likelihood: float) -> float:
    """
    Computes the Bayesian Information Criterion (BIC) for a Gaussian mixture model.

    The BIC is a criterion for model selection that balances model fit (measured by
    log-likelihood) against model complexity. It is calculated as:

    BIC = ln(L) - 0.5 * k * ln(n)

    where:
    - ln(L) is the log-likelihood
    - k is the number of free parameters in the model
    - n is the number of data points

    Args:
        X: Data array of shape (n, d) where:
           - n is the number of samples
           - d is the dimension of each sample
        mixture: GaussianMixture object containing:
                - mu: (K, d) array of K component means
                - var: (K,) array of K component variances
                - p: (K,) array of K mixing coefficients
        log_likelihood: The log-likelihood of the data under the model

    Returns:
        float: BIC score. Lower values indicate better model fit,
               accounting for model complexity.
    """

    n, d = X.shape
    return log_likelihood - 0.5 * (d * len(mixture.mu) +
                                   len(mixture.var) +
                                   len(mixture.p) - 1) * np.log(n)
