# Lab 4: Regression and Classification Evaluation Metrics

Part 1: Comprehensive Study of K-Nearest Neighbours (KNN) Classification using Breast Cancer Dataset and Comparison with Regression Evaluation Metrics.

## Aim

To implement KNN classification on the Breast Cancer dataset and analyze model performance using train-test split, heuristic K selection, cross-validation, ROC-AUC, and classification metrics. Also, to compare classification metrics with regression metrics studied in Linear Regression (Lab 3).

## Dataset

Breast Cancer Wisconsin (Diagnostic) Dataset

- UCI: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- Kaggle: https://www.kaggle.com/datasets/utkarshx27/breast-cancer-wisconsin-diagnostic-dataset
- CSV: https://drive.google.com/file/d/1poP5CatfiZGaRbGCAKPGe_wOBCGspDjA/view?usp=drive_link

Dataset details:

- 569 samples
- 30 numerical features
- Binary target

## Problem Statement

A healthcare analytics team is developing a predictive model for early cancer detection. You are required to build a KNN classifier, optimize its performance using different validation techniques, and compare classification evaluation metrics with regression evaluation metrics from Lab 3.

## Tasks

### Task 1: Data Preparation

1. Load the dataset using `sklearn`.
2. Convert into DataFrame and explore structure.
3. Check missing values and duplicates.
4. Apply feature scaling using `StandardScaler` and justify its importance.

### Task 2: Train-Test Split Analysis

1. Split dataset into training and testing sets (80:20).
2. Repeat with 70:30 and 90:10 splits.
3. Compare performance variations across splits.
4. Analyze how dataset splitting affects model stability and generalization.

### Task 3: KNN Model with Heuristic K Selection

#### 3.1 Heuristic Method for K Selection

1. Compute initial K using heuristic rule: K = sqrt(n), where n = number of training samples.
2. Use this value as a baseline K.

#### 3.2 Model Training

1. Train KNN classifier using heuristic K value.
2. Experiment with nearby values of K (K +/- 5).
3. Plot accuracy vs K values.
4. Identify optimal K based on performance trend.

#### 3.3 Distance Matrix and Decision Boundary Mapping

1. Explain any two distance metrics used in KNN: Euclidean Distance and Manhattan Distance. Also mention when each distance metric is suitable.
2. Plot the decision boundary of the KNN classifier for different values of K, such as K = 1, K = 5, K = 10, and K = 20. Analyze how the decision boundary changes as K increases.

### Task 4: Cross Validation

1. Apply K-Fold Cross Validation (k = 5 or 10).
2. Compute mean accuracy for different K values.
3. Compare cross-validation results with train-test split results.
4. Select best K based on both heuristic and validation results.

### Task 5: Classification Evaluation

Evaluate final model using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve and AUC Score

### Task 6: Comparative Study with Regression (Lab 3 Integration)

Reference: Recall Lab 3 (Linear Regression) where you evaluated:

- MAE
- MSE
- RMSE
- R2 Score

Tasks:

1. Compare regression evaluation metrics with classification metrics.
2. Explain differences between both metric families.
3. Compare interpretation of errors vs decision outcomes.
4. Discuss differences in evaluation logic for regression and classification.

Inference requirement (short and precise - do not generate):

Write a detailed inference covering:

- How regression metrics measure prediction error magnitude
- How classification metrics measure decision correctness
- Why accuracy is insufficient in medical diagnosis
- Why recall and ROC-AUC are more relevant in healthcare
- Overall comparison between regression and classification evaluation frameworks

### Task 7: Analytical Questions

1. Why is KNN called a lazy learning algorithm?
2. Why is feature scaling required in KNN?
3. Explain heuristic K selection using sqrt(n) rule.
4. Why is cross-validation more reliable than a single train-test split?
5. How does K affect bias-variance trade-off?
6. Why is recall more important than accuracy in cancer prediction?
7. What is the limitation of very large K values?

## Expected Outcome

- Understanding of KNN algorithm and distance-based learning
- Ability to tune K using heuristic and validation
- Knowledge of cross-validation
- Interpretation of ROC-AUC in medical classification
- Strong conceptual link between regression and classification evaluation metrics

## Conclusion

Students should summarize:

- Optimal K value using sqrt(n) and validation
- Effect of train-test split variations
- Model performance based on evaluation metrics
- Key differences between regression and classification evaluation
- Insights from Lab 3 vs current lab
