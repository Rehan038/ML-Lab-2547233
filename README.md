# ML Lab Repository Overview

This repository contains the notebook work for Labs 1, 3, 4, 5, and 6. This page is the main entry point for the repository and gives a quick summary of each lab for evaluation.

## Lab Summary

### Lab 1: Data Exploration and Preprocessing
- Folder: [ML-LAB1](ML-LAB/ML-LAB1)
- Focus: dataset inspection, preprocessing, and introductory notebook work.
- Includes the Lab 1 notebook and supporting datasets.

### Lab 3: Linear Regression Evaluation
- Focus: regression evaluation and error measurement.
- Key metrics: MAE, MSE, RMSE, and R².
- Lab 3 is referenced later in Lab 4 when comparing regression and classification evaluation.

### Lab 4: KNN Classification and Metric Comparison
- Folder: [ML Lab4](ML-LAB/ML%20Lab4)
- Focus: KNN classification on the Breast Cancer Wisconsin dataset.
- Covers train-test split analysis, heuristic K selection, cross-validation, ROC-AUC, and comparison with regression metrics from Lab 3.

### Lab 5: Linear Regression Through Gradient Descent
- Folder: [ML-lab5](ML-LAB/ML-lab5)
- Focus: implementing linear regression from scratch using gradient descent.
- Covers preprocessing, feature scaling, learning-rate experiments, convergence plots, and regression metrics.

### Lab 6: Logistic Regression vs KNN Classification
- Folder: [ML-lab6](ML-LAB/ML-lab6)
- Focus: comparing Logistic Regression and KNN on the Breast Cancer Wisconsin dataset.
- Covers preprocessing, standardization, classification metrics, confusion matrices, and ROC-AUC.

## Repository Structure

- `ML-LAB1/` - Lab 1 notebook and dataset files
- `ML Lab4/` - Lab 4 notebook and README
- `ML-lab5/` - Lab 5 notebook and README
- `ML-lab6/` - Lab 6 notebook and README
- `dataset/` - shared datasets used by multiple labs

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
- Labs 4 and 6 are classification-focused and compare models using accuracy, precision, recall, F1 score, confusion matrix, and ROC-AUC.
- Lab 5 focuses on a custom gradient descent implementation rather than using a built-in regression estimator only.
- Lab 3 provides the regression metrics referenced by later labs.

