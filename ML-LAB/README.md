# ML Lab Repository Overview

This repository contains the notebooks and supporting files for Labs 1, 3, 4, 5, 6, 7, 8, and 9. The goal of this README is to give an evaluator a single, clean entry point to the work in the repository.

## Lab Summary

### Lab 1: Data Exploration and Preprocessing
- Folder: `ML-LAB1/`
- Focus: basic data exploration, dataset inspection, and preprocessing.
- Includes the Lab 1 notebook and supporting datasets.

### Lab 3: Linear Regression Evaluation
- Focus: regression metrics and model evaluation.
- Key ideas: MAE, MSE, RMSE, and R².
- This lab is referenced later in Lab 4 when comparing regression and classification evaluation.

### Lab 4: KNN Classification and Metric Comparison
- Folder: `ML Lab4/`
- Focus: K-Nearest Neighbors classification on the Breast Cancer Wisconsin dataset.
- Covers train-test split analysis, heuristic K selection, cross-validation, ROC-AUC, and comparison with regression metrics from Lab 3.

### Lab 5: Linear Regression Through Gradient Descent
- Folder: `ML-lab5/`
- Focus: implementing linear regression from scratch using gradient descent.
- Covers preprocessing, feature scaling, learning-rate experiments, convergence plots, and regression metrics.

### Lab 6: Logistic Regression vs KNN Classification
- Folder: `ML-lab6/`
- Focus: comparing Logistic Regression and KNN on the Breast Cancer Wisconsin dataset.
- Covers preprocessing, standardization, classification metrics, confusion matrices, and ROC-AUC.

### Lab 7: Decision Tree Classification on Iris
- Folder: `ML-Lab7/`
- Focus: Iris dataset exploration, train-test splitting, and Decision Tree classification.
- Covers dataset inspection, model evaluation with accuracy, confusion matrix, classification report, and tree visualization.

### Lab 8: Categorical Naive Bayes on Weather Data
- Folder: `ML-Lab8/`
- Focus: play-tennis style weather classification using categorical features.
- Covers label encoding, train-test split, Categorical Naive Bayes, evaluation metrics, and single-sample inference.

### Lab 9: SVM, PCA, and LDA
- Folder: `ML-Lab9/`
- Focus: binary classification with SVM and dimensionality reduction with PCA and LDA.
- Covers feature scaling, hyperparameter tuning, confusion matrix analysis, explained variance, and PCA vs LDA comparison.

## Repository Structure

- `ML-LAB1/` - Lab 1 notebook and supporting data
- `ML Lab4/` - Lab 4 notebook and README
- `ML-lab5/` - Lab 5 notebook and README
- `ML-lab6/` - Lab 6 notebook and README
- `ML-Lab7/` - Lab 7 notebook and README
- `ML-Lab8/` - Lab 8 notebook and README
- `ML-Lab9/` - Lab 9 notebook and README
- `dataset/` - shared datasets used by the notebooks

## How to Run

1. Open the repository in VS Code or Jupyter.
2. Install the required Python packages if needed:

```bash
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn notebook
```

3. Open the notebook for the desired lab and run the cells in order.

## Notes for Evaluation

- Each lab folder has its own README for a short lab-specific summary.
- Lab 4 and Lab 6 are classification-focused and compare models using accuracy, precision, recall, F1 score, confusion matrix, and ROC-AUC.
- Lab 5 focuses on a custom gradient descent implementation rather than a library-only linear regression call.
- Lab 3 provides the regression metrics referenced in later labs.
- Lab 7 uses the Iris dataset with a Decision Tree classifier.
- Lab 8 uses categorical encoding with Naive Bayes for weather-based classification.
- Lab 9 combines SVM classification with PCA and LDA analysis.