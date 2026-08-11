# Lab 7: Decision Tree Classification on Iris

## Overview
This lab explores the Iris dataset, splits the data into training and testing sets, and trains a Decision Tree classifier to predict the flower class.

## Notebook Flow
1. Load the Iris dataset from `sklearn`.
2. Inspect the number of samples, number of features, feature names, target classes, and class distribution.
3. Build an 80:20 train-test split with `random_state=42`.
4. Train a `DecisionTreeClassifier` with default parameters.
5. Evaluate the model using accuracy, confusion matrix, and classification report.
6. Visualize the trained decision tree.

## Key Observations
- The Iris dataset has 150 samples and 4 features.
- The three classes are evenly distributed.
- The Decision Tree achieved 100% accuracy on the test set in this notebook.
- The confusion matrix shows no misclassifications.

## Files
- `25472133Lab7.ipynb`: main notebook
- `README.md`: summary for evaluator review

## Conclusion
The notebook demonstrates a complete classification workflow on a simple multiclass dataset and shows how Decision Trees can separate the Iris classes very effectively.
