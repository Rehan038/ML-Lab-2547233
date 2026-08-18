# Machine Learning Lab 4: K-Nearest Neighbors (KNN) & Classification vs. Regression Analysis

## 📌 Overview
This lab provides an in-depth investigation of the **K-Nearest Neighbors (KNN)** classification algorithm on the Wisconsin Breast Cancer Diagnostic dataset. It covers train-test splitting dynamics, heuristic and empirical hyperparameter tuning ($K$), distance metric formulations, decision boundary visualization, cross-validation pipelines, and a comparative study contrasting classification with continuous regression framing.

---

## 🎯 Objectives
- **Data Standardization & Feature Scaling**:
  - Implement `StandardScaler` on multi-dimensional clinical measurements to prevent high-magnitude features from dominating Euclidean distance calculations.
- **Train-Test Split Stability Analysis**:
  - Compare model stability and variance across multiple split ratios ($80:20$, $70:30$, and $90:10$).
- **Optimal Hyperparameter Selection ($K$)**:
  - Establish a baseline using the square-root heuristic: $K = \sqrt{N_{\text{train}}}$.
  - Perform hyperparameter grid search across odd neighbor values ($K \pm 5$) to prevent ties.
  - Implement **$K$-Fold Cross Validation ($5$-Fold)** within a `Pipeline` to prevent data leakage and evaluate generalizability.
- **Decision Boundary Visualization**:
  - Plot 2D decision surfaces across varying values of $K$ ($K=1, 5, 10, 20$) to illustrate overfitting (high variance) vs. underfitting (high bias / over-smoothing).
- **Comprehensive Classification Evaluation**:
  - Calculate Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC curve, and Area Under the Curve (ROC-AUC).
- **Comparative Study: KNN vs. Linear Regression**:
  - Frame the binary diagnosis problem through continuous linear regression thresholding and contrast loss measurement methodologies (MSE/MAE vs. Log-loss/Confusion Matrix).

---

## 📊 Dataset Description
- **Breast Cancer Wisconsin (Diagnostic) Dataset**:
  - 569 instances with 30 continuous features computed from digitized images of fine needle aspirates (FNA) of breast masses (mean, standard error, and worst values of radius, texture, perimeter, area, smoothness, compactness, concavity, etc.).
  - Target: Diagnosis (Malignant `0` / Benign `1`).

---

## 🔬 Lab Tasks & Key Experiments

| Task | Focus Area | Key Methods / Metrics |
| :--- | :--- | :--- |
| **Task 1: Data Preparation** | Exploration, zero null/duplicate verification, z-score standardization | `StandardScaler()`, `pd.DataFrame.describe()` |
| **Task 2: Split Sensitivity** | Evaluation of split ratios ($80:20$, $70:30$, $90:10$) on test accuracy & variance | `train_test_split()`, variance trade-off analysis |
| **Task 3: Heuristic $K$ & Distance Metrics** | Testing $K=\sqrt{n}$, comparing Euclidean vs. Manhattan distance, decision boundaries | `KNeighborsClassifier()`, 2D meshgrid contour plots |
| **Task 4: Cross-Validation Pipeline** | Leak-free $5$-Fold Cross Validation across neighbor candidate range | `Pipeline([('scaler', StandardScaler()), ('knn', ...)])`, `cross_val_score` |
| **Task 5: Complete Evaluation** | Final model evaluation on unseen test data | Accuracy, Precision, Recall, F1, Confusion Matrix, ROC-AUC |
| **Task 6: Regression Comparison** | Reformulating classification into Continuous Linear Regression | `LinearRegression()`, MAE/MSE vs. Classification Report |
| **Task 7: Conceptual Analysis** | Explaining why KNN is a "Lazy Learner" (instance-based non-parametric) | Memory complexity, query-time computation analysis |

---

## 💡 Key Takeaways & Insights
- **Scaling Importance**: Without feature scaling, distance-based algorithms like KNN fail due to distortion from arbitrary feature units.
- **Decision Boundary Dynamics**: Small values ($K=1$) yield complex, fragmented decision boundaries prone to noise overfitting; large values of $K$ oversmooth boundary transitions.
- **Cross-Validation Superiority**: Cross-validated hyperparameter search identified an optimal balance ($K=17$) that achieved peak generalizability without single-split variance biases.
- **Classification vs. Regression**: Linear regression with arbitrary thresholding lacks probabilistic calibration for boundary regions, whereas KNN natively outputs posterior neighborhood probabilities.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
Open and run [`ML-LAB4.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB4/ML-LAB4.ipynb) in Jupyter Notebook or VS Code.
