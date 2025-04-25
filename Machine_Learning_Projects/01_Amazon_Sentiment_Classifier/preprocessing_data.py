"""
This module provides functionality for processing and preparing text data for sentiment analysis.
It includes tools for loading reviews data, text tokenization, and feature extraction using
the bag-of-words approach.
"""

import csv
from string import punctuation, digits
import numpy as np
import random

def load_data(path_data):
    """
    Loads and processes review data from a TSV file containing sentiment analysis data.

    Args:
        path_data (str): Path to the TSV file containing the review data

    Returns:
        list: A list of dictionaries, where each dictionary represents a review with keys:
            - 'sentiment': int, either +1 (positive) or -1 (negative)
            - 'text': str, the text content of the review

    Note:
        - The file is expected to be TSV (tab-separated values) format
        - File is read using 'latin1' encoding
        - Only 'sentiment' and 'text' fields are kept from the input file
        - Numeric fields (sentiment) are converted to integers
        - All other fields in the input file are discarded
    """

    basic_fields = {'sentiment', 'text'}
    numeric_fields = {'sentiment', 'helpfulY', 'helpfulN'}

    data = []

    f_data = open(path_data, encoding="latin1")

    # Use csv.DictReader to read the TSV file
    # delimiter='\t' specifies that fields are separated by tabs
    # This creates dictionaries where keys are column headers and values are the data
    for datum in csv.DictReader(f_data, delimiter='\t'):
        for field in list(datum.keys()):
            if field not in basic_fields:
                del datum[field]
            elif field in numeric_fields and datum[field]:
                datum[field] = int(datum[field])
        data.append(datum)

    f_data.close()

    return data


def extract_words(text):
    """
    Preprocesses and tokenizes a text string into individual words and special characters.

    This function performs the following operations:
    1. Adds spaces around all punctuation marks and digits
    2. Converts the text to lowercase
    3. Splits the text into individual tokens

    Args:
        text (str): The input text string to be processed

    Returns:
        list: A list of strings where each string is either:
            - A lowercase word
            - A single punctuation mark
            - A single digit

    Example:
        >>> extract_words("Hello, World! 123")
        ['hello', ',', 'world', '!', '1', '2', '3']
    """

    for c in punctuation + digits:
        text = text.replace(c, ' ' + c + ' ')
    return text.lower().split()



def bag_of_words(texts):
    """
    Creates a vocabulary dictionary from a collection of texts using the bag-of-words model.

    The function processes each text by:
    1. Extracting words (using extract_words function)
    2. Creating a mapping of unique words to indices
    3. Assigning indices sequentially as new words are encountered

    Args:
        texts (list): A list of strings where each string is a text document/review

    Returns:
        dict: A dictionary where:
            - keys are unique words from all texts (lowercased)
            - values are unique integer indices (0 to N-1, where N is vocabulary size)

    Example:
        >>> texts = ["He loves her", "He really really loves her"]
        >>> bag_of_words(texts)
        {'he': 0, 'loves': 1, 'her': 2, 'really': 3}
    """

    indices_by_word = {}  # maps word to unique index
    for text in texts:
        word_list = extract_words(text)
        for word in word_list:
            if word in indices_by_word:
                continue
            indices_by_word[word] = len(indices_by_word)
    return indices_by_word

def extract_bow_feature_vectors(reviews,
                                indices_by_word,
                                binarize=True):
    """
    Creates a feature matrix from text reviews using bag-of-words representation.

    Args:
        reviews (list): List of text reviews/strings to be converted
        indices_by_word (dict): Dictionary mapping words to their unique indices
        binarize (bool, optional): If True, creates binary features (0/1) indicating word presence.
                                 If False, counts word occurrences in each review.
                                 Defaults to True.

    Returns:
        np.ndarray: A matrix of shape (n, m) where:
            - n is the number of reviews
            - m is the number of unique words in the dictionary
            When binarize=True:
                Each cell [i,j] contains 1 if word j appears in review i, 0 otherwise
            When binarize=False:
                Each cell [i,j] contains the number of times word j appears in review i
    """


    feature_matrix = np.zeros([len(reviews), len(indices_by_word)],
                              dtype=np.float64)
    for i, text in enumerate(reviews):
        word_list = extract_words(text)
        for word in word_list:
            if word not in indices_by_word: continue
            if binarize: feature_matrix[i, indices_by_word[word]] = 1
            else: feature_matrix[i, indices_by_word[word]] += 1
    return feature_matrix


def train_test_data_extract(binary):
    """
    Extracts and prepares training and test data for sentiment analysis.

    Args:
        binary (bool): If True, creates binary feature vectors (0/1),
                       If False, uses word count features.

    Returns:
        tuple: Contains four elements:
            - train_bow_features (np.ndarray): Feature matrix for training data
            - train_labels (tuple): Sentiment labels for training data
            - test_bow_features (np.ndarray): Feature matrix for test data
            - test_labels (tuple): Sentiment labels for test data
    """

    train_data = load_data('reviews_train.tsv')
    test_data = load_data('reviews_test.tsv')

    train_texts, train_labels = zip(*((sample['text'],
                                       sample['sentiment'])
                                      for sample in train_data))
    test_texts, test_labels = zip(*((sample['text'],
                                     sample['sentiment'])
                                    for sample in test_data))

    dictionary = bag_of_words(train_texts)


    train_bow_features = extract_bow_feature_vectors(train_texts,
                                                     dictionary,
                                                     binary)
    test_bow_features = extract_bow_feature_vectors(test_texts,
                                                    dictionary,
                                                    binary)

    return train_bow_features, train_labels, test_bow_features, test_labels, dictionary

if __name__ == '__main__':
    train_data0 = load_data('reviews_train.tsv')
    train_texts0, train_labels0 = zip(*((sample['text'],
                                       sample['sentiment'])
                                      for sample in train_data0))

    dictionary0 = bag_of_words(train_texts0)

    print(extract_bow_feature_vectors(train_texts0, dictionary0, False))
