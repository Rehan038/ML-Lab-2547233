# Lab 8: Categorical Naive Bayes on Weather Data

## Overview
This lab uses a small weather dataset to predict whether tennis should be played, then applies a Categorical Naive Bayes classifier after encoding the categorical features.

## Notebook Flow
1. Load the dataset from `lab8.csv`.
2. Inspect the head, summary statistics, column names, shape, and data types.
3. Encode categorical columns using `LabelEncoder`.
4. Split the encoded data into training and testing sets with an 80:20 ratio.
5. Train a `CategoricalNB` model.
6. Evaluate the model using accuracy, confusion matrix, and classification report.
7. Run a single-sample inference for a specific weather condition.

## Key Observations
- The dataset is small and fully categorical.
- Label encoding is required before training `CategoricalNB`.
- The notebook includes both model evaluation and a prediction example for a new weather record.

## Files
- `2547233_Lab8.ipynb`: main notebook
- `README.md`: summary for evaluator review

## Conclusion
The notebook demonstrates a complete categorical classification pipeline and shows how Naive Bayes can be used for simple rule-like prediction tasks.
