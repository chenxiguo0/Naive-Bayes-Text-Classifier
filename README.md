[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/pEbqUUJs)

# Naive Bayes Text Classifier

## Project Overview

This project implements a Naive Bayes text classifier in Python designed to predict authorship based on text data. The classifier is trained on labeled text files, where each author is associated with a unique set of text samples. The program tokenizes text by splitting it along whitespace and calculates class priors and word likelihoods using term frequency.


It contains three key components:

    NaiveBayes Class: Located in nb.py, this class includes methods to train (train) and test (test) the Naive Bayes model.
    
    build_dataframe Function: Defined in load_data.py, this utility function loads the text data from specified directories into training and test DataFrames.
    
    main.py Script: This is the entry point for running the classifier, using argparse to specify data locations and output predictions.
    
1. **NaiveBayes Class**: Located in `nb.py`, this class contains methods to train (`train`) and test (`test`) the Naive Bayes model.
2. **build_dataframe Function**: Defined in `load_data.py`, this utility function loads text data from specified directories into training and test DataFrames.
3. **main.py Script**: The entry point for running the classifier, which uses `argparse` to specify the data locations and output predictions.



Running the Classifier

Run main.py with a specified data directory containing subfolders for each author. These subfolders should contain text files for training, and there should be a separate unlabeled folder for testing.

Run python nb/bin/main.py -f /path/to/data

And replace /path/to/data with the relative or absolute path to the required data directory.

The project will output:

    The training data details (priors and likelihoods).
    
    The predictions for each test sample, including the text and the predicted author.
