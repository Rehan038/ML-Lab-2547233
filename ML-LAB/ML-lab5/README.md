# Lab 5: Linear Regression through Gradient Descent

## Aim
Implement linear regression using gradient descent and study how different learning rates affect convergence and prediction quality.

## Dataset
Student Performance dataset (`student-mat.csv`), which contains student records, demographic details, study habits, and the target grade `G3`.

## Workflow
1. Load the dataset with pandas.
2. Inspect the structure, summary statistics, missing values, and duplicates.
3. Encode categorical variables using one-hot encoding.
4. Separate features and target.
5. Standardize the feature set with `StandardScaler`.
6. Split the data into 70% training and 30% testing sets.
7. Train a linear regression model using a custom gradient descent function.
8. Experiment with learning rates to study convergence behavior.
9. Plot the cost history across iterations.
10. Evaluate the final model using MAE, MSE, RMSE, and R².

## Key Observations
- The dataset has 395 student records and 33 features.
- There are no missing values and no duplicate rows in the dataset.
- Feature scaling improves gradient descent convergence.
- Larger learning rates converge faster, while very small learning rates slow training.
- The best observed learning rates in the notebook were `0.05` and `0.1`.

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Conclusion
Gradient descent successfully learned the relationship between the input features and the final grade. The model achieved relatively low prediction error, and the convergence plots show the impact of learning rate on optimization speed.
