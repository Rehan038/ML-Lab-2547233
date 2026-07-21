# Lab 5: Linear Regression Through Gradient Descent

## Overview
This notebook implements linear regression from scratch using the gradient descent algorithm and studies how the learning rate affects convergence.

## Dataset
The notebook uses the Student Performance dataset from `student-mat.csv`.

Dataset characteristics:
- 395 student records
- 33 features
- Target variable: `G3` final grade

## Notebook Flow
1. Load the dataset with pandas.
2. Inspect the shape, columns, summary statistics, missing values, and duplicates.
3. Convert categorical variables to numeric form using one-hot encoding.
4. Separate the feature matrix `X` and target vector `y`.
5. Standardize the features with `StandardScaler`.
6. Split the data into 70% training and 30% testing sets.
7. Train linear regression with a custom gradient descent function.
8. Compare multiple learning rates to observe convergence speed.
9. Plot the cost history across iterations.
10. Evaluate the final model using regression metrics.

## Key Observations
- The dataset contains zero missing values and zero duplicate rows.
- Feature scaling improves gradient descent convergence.
- Small learning rates converge slowly.
- Larger learning rates converge faster on this dataset.
- The notebook shows the best practical convergence around learning rates `0.05` and `0.1`.

## Final Evaluation
The trained model produced the following test results:
- MAE: 1.5251
- MSE: 4.9930
- RMSE: 2.2345
- R²: 0.7729

## Files
- `Lab5.ipynb`: main notebook
- `README.md`: summary for evaluator review

## Conclusion
Gradient descent successfully learned the relationship between the student features and final grade. The model achieved a reasonable error level and a strong R² score, showing that the notebook demonstrates both optimization behavior and prediction performance clearly.