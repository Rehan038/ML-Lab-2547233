# Lab 6: Logistic Regression vs KNN Classification

## Aim
Compare Logistic Regression and K-Nearest Neighbors (KNN) classifiers on the Breast Cancer Wisconsin (Diagnostic) dataset and evaluate their performance using standard classification metrics.

## Dataset
Breast Cancer Wisconsin (Diagnostic) dataset with 569 samples and 30 numerical features.

## Workflow
1. Load the dataset with pandas.
2. Inspect data shape, structure, summary statistics, and missing values.
3. Remove the `ID` column.
4. Map the diagnosis labels to binary values.
5. Separate features and target.
6. Standardize the feature set using `StandardScaler`.
7. Split the dataset into training and testing sets.
8. Train a Logistic Regression classifier.
9. Train a KNN classifier.
10. Compare both models using accuracy, precision, recall, F1 score, confusion matrix, and ROC-AUC.

## Key Observations
- The dataset was clean, with no missing values and no duplicate rows.
- Feature scaling is important for both Logistic Regression and KNN.
- Logistic Regression performed better than KNN in the notebook results.
- Logistic Regression made fewer incorrect predictions and produced a stronger ROC curve.

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve and AUC

## Conclusion
The notebook shows that Logistic Regression outperformed KNN on this dataset. The comparison also highlights how different classification metrics provide complementary views of model quality.
