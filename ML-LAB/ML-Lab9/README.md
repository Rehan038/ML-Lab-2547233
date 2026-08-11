# Lab 9: SVM, PCA, and LDA

## Overview
This lab combines supervised classification and dimensionality reduction by training an SVM on the Breast Cancer dataset and comparing PCA and LDA on the Wine dataset.

## Notebook Flow
### Part A: SVM Classification
1. Load the Breast Cancer Wisconsin dataset.
2. Inspect shape, class distribution, missing values, and the first rows.
3. Split the data into training and testing sets using an 80:20 ratio with stratification.
4. Standardize the features with `StandardScaler`.
5. Tune the SVM regularisation parameter `C` with `GridSearchCV`.
6. Train a linear-kernel SVM and evaluate it using classification metrics and a confusion matrix.

### Part B: PCA on Wine Dataset
1. Load and standardize the Wine dataset.
2. Reduce the data to 2 principal components using PCA.
3. Compute explained variance ratios and cumulative variance.
4. Plot the PCA projection and component loadings.

### Extension: LDA
1. Apply Linear Discriminant Analysis to the Wine dataset.
2. Project the data into 2 discriminant components.
3. Compare PCA and LDA side by side.

## Key Observations
- The SVM model achieves very strong classification performance on the Breast Cancer dataset.
- Standard scaling is important for SVM stability and performance.
- PCA preserves the most variance, while LDA produces clearer class separation for the Wine dataset.

## Files
- `2547233_Lab9.ipynb`: main notebook
- `README.md`: summary for evaluator review

## Conclusion
The notebook shows both model tuning for classification and a practical comparison between unsupervised and supervised dimensionality reduction techniques.