# Lab 6: Logistic Regression vs KNN Classification

## Overview
This notebook compares Logistic Regression and K-Nearest Neighbors (KNN) classifiers on a breast cancer diagnosis dataset and evaluates both models using standard classification metrics.

## Dataset
The notebook uses the Breast Cancer Wisconsin (Diagnostic) dataset.

Dataset characteristics:
- 569 samples
- 30 numerical features
- Binary target: malignant or benign diagnosis

## Notebook Flow
1. Load the dataset with pandas.
2. Inspect the shape, data types, summary statistics, missing values, and duplicates.
3. Remove the `ID` column.
4. Map diagnosis labels to binary values.
5. Separate features and target.
6. Standardize the feature set with `StandardScaler`.
7. Split the data into training and testing sets.
8. Train a Logistic Regression classifier.
9. Train a KNN classifier.
10. Compare both models using classification metrics and ROC-AUC.

## Key Observations
- The dataset contains no missing values and no duplicate rows.
- Feature scaling is important for both Logistic Regression and KNN.
- Logistic Regression performed better than KNN on this dataset.
- Logistic Regression produced fewer false positives and false negatives.
- The ROC curve for Logistic Regression was stronger and closer to the top-left corner.

## Final Evaluation
Logistic Regression:
- Accuracy: 0.9825
- Precision: 0.9688
- Recall: 0.9841
- F1 Score: 0.9764
- Confusion Matrix: [[106, 2], [1, 62]]

KNN:
- Accuracy: 0.9591
- Precision: 0.9516
- Recall: 0.9365
- F1 Score: 0.9440
- Confusion Matrix: [[105, 3], [4, 59]]

## Files
- `Lab6.ipynb`: main notebook
- `README.md`: summary for evaluator review

## Conclusion
The notebook clearly shows that Logistic Regression outperformed KNN on this dataset. The comparison is also useful for understanding how different metrics describe different aspects of model quality.
