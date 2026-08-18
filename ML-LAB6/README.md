# Machine Learning Lab 6: Comparative Analysis of Logistic Regression and K-Nearest Neighbors (KNN)

## 📌 Overview
This lab presents a rigorous comparative benchmark between a parametric linear classifier (**Logistic Regression**) and a non-parametric instance-based classifier (**$K$-Nearest Neighbors / KNN**) applied to clinical breast tumor diagnosis.

---

## 🎯 Objectives
- **Data Preprocessing & Standardization**:
  - Load the Breast Cancer Wisconsin (Diagnostic) dataset (`wdbc.data`).
  - Standardize 30 continuous geometrical features using `StandardScaler` to ensure zero mean and unit variance.
  - Encode binary diagnosis labels (`M` = Malignant $\rightarrow 1$, `B` = Benign $\rightarrow 0$).
- **Logistic Regression Classifier**:
  - Train a linear probabilistic model using standard maximum likelihood / cross-entropy loss minimization.
- **K-Nearest Neighbors Classifier**:
  - Train a distance-based classifier using optimal neighbor neighborhood querying ($K=5$).
- **Comprehensive Comparative Evaluation**:
  - Compare both models on identical test partitions across all key classification metrics:
    - **Accuracy**: Overall fraction of correct predictions.
    - **Precision**: Specificity in malignant classification ($\frac{TP}{TP + FP}$).
    - **Recall (Sensitivity)**: Ability to capture all true positive cases ($\frac{TP}{TP + FN}$).
    - **F1-Score**: Harmonic mean of Precision and Recall.
    - **Confusion Matrix**: Detailed count of True Positives, True Negatives, False Positives, and False Negatives.

---

## 📊 Dataset Description
- **Wisconsin Diagnostic Breast Cancer (WDBC)**:
  - 569 patient records.
  - 30 nuclear feature attributes (e.g., radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, fractal dimension).
  - Target: Binary clinical classification (`Malignant` vs. `Benign`).

---

## 🔬 Experimental Workflow & Comparison

```
Raw WDBC Data ──► Missing Value Check ──► Standardization (StandardScaler) ──► Train/Test Split (80:20)
                                                                                         │
                                                    ┌────────────────────────────────────┴───────────────────────────────────┐
                                                    ▼                                                                        ▼
                                     Logistic Regression Classifier                                            KNN Classifier (K=5)
                                                    │                                                                        │
                                                    └────────────────────────────────────┬───────────────────────────────────┘
                                                                                         ▼
                                                                Performance Metrics & Confusion Matrix Comparison
```

---

## 📈 Benchmark Results Summary

| Metric | Logistic Regression | K-Nearest Neighbors (KNN) | Advantage / Winning Model |
| :--- | :--- | :--- | :--- |
| **Accuracy** | **~97.4%** | ~93.9% | **Logistic Regression** |
| **Precision** | **~97.6%** | ~95.0% | **Logistic Regression** |
| **Recall** | **~95.3%** | ~88.4% | **Logistic Regression** (Crucial in medical diagnosis) |
| **F1-Score** | **~96.4%** | ~91.6% | **Logistic Regression** |
| **Misclassifications** | **3 incorrect** | 7 incorrect | **Logistic Regression** |

---

## 💡 Key Takeaways & Clinical Interpretation
1. **Medical Impact of High Recall**: In cancer diagnostics, **False Negatives (FN)** (classifying a malignant tumor as benign) pose catastrophic clinical risks. Logistic Regression achieved significantly higher Recall (~95.3% vs. ~88.4%), minimizing dangerous false reassurance.
2. **Curse of Dimensionality**: With 30 continuous features, KNN suffers from distance concentration in higher-dimensional space, whereas Logistic Regression finds an optimal hyperplanar linear decision boundary that separates the two classes with higher margin confidence.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
Open and run [`ML-LAB6.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB6/ML-LAB6.ipynb) in Jupyter Notebook or VS Code.
