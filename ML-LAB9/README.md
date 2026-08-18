# Machine Learning Lab 9: Support Vector Machines (SVM), PCA, and LDA

## 📌 Overview
This lab implements **Support Vector Machines (SVM)** for classification along with two prominent dimensionality reduction techniques: **Principal Component Analysis (PCA)** (unsupervised variance maximization) and **Linear Discriminant Analysis (LDA)** (supervised class-separability maximization).

---

## 🎯 Objectives

### Part A: Support Vector Machine (SVM)
- **Clinical Classification**:
  - Load the Breast Cancer Wisconsin dataset (30 features, binary diagnosis).
  - Apply `StandardScaler` to normalize feature magnitudes.
  - Split dataset into 80% training and 20% testing sets.
- **Hyperparameter Optimization (`GridSearchCV`)**:
  - Tune the regularization parameter $C \in \{0.01, 0.1, 1, 10, 100\}$ on a linear kernel.
  - Understand the margin trade-off: small $C$ (soft margin, higher tolerance for violations) vs. large $C$ (hard margin, penalizes violations heavily).
- **Evaluation**:
  - Evaluate accuracy, precision, recall, F1-score, and display the confusion matrix.

### Part B: Principal Component Analysis (PCA)
- **Unsupervised Dimensionality Reduction**:
  - Load the multi-class **Wine Recognition Dataset** (13 features, 3 classes).
  - Standardize features and project from 13 dimensions down to 2 principal components:
    $$\text{Maximize } \text{Var}(X \mathbf{w}) \quad \text{subject to } \|\mathbf{w}\| = 1$$
- **Variance Analysis**:
  - Compute individual Explained Variance Ratio for PC1 and PC2.
  - Compute the cumulative variance curve across all 13 components to find the number of dimensions needed to preserve $\ge 95\%$ variance.
- **Visualization & Loadings Interpretation**:
  - Plot 2D scatter plots of transformed samples colored by wine cultivars.
  - Analyze eigenvector feature loadings to interpret the physical meaning of PC1 and PC2.

### Part C: Linear Discriminant Analysis (LDA) & Comparison
- **Supervised Dimensionality Reduction**:
  - Apply LDA to project the Wine dataset onto 2 discriminant directions that maximize the Fisher criterion:
    $$J(\mathbf{w}) = \frac{\mathbf{w}^T \mathbf{S}_B \mathbf{w}}{\mathbf{w}^T \mathbf{S}_W \mathbf{w}} = \frac{\text{Between-Class Scatter}}{\text{Within-Class Scatter}}$$
- **Comparative Visual Analysis**:
  - Side-by-side comparison of 2D PCA vs. 2D LDA scatter plots.

---

## 📊 Datasets Description
1. **Breast Cancer Wisconsin Dataset**: 569 instances, 30 features, binary class (Malignant vs. Benign).
2. **Wine Recognition Dataset**: 178 instances, 13 chemical constituents (alcohol, malic acid, ash, flavanoids, color intensity, proline, etc.), 3 wine cultivator cultivars.

---

## 🔬 Lab Workflow & Key Experiments

| Section | Method / Tool | Core Purpose / Metric |
| :--- | :--- | :--- |
| **Part A: SVM** | `SVC(kernel='linear')`, `GridSearchCV` | Maximal margin hyperplane classification, $C$ parameter tuning |
| **Part B: PCA** | `PCA(n_components=2)`, `StandardScaler` | Unsupervised orthogonal projection, explained variance ratio |
| **Part B: Cumulative Variance**| `numpy.cumsum(pca.explained_variance_ratio_)` | Determining optimal components to retain $\ge 95\%$ information |
| **Part C: LDA** | `LinearDiscriminantAnalysis(n_components=2)`| Supervised class separation maximizing between/within scatter |
| **Synthesis** | Side-by-side 2D Projection Plots | Visual comparison of unsupervised variance vs. supervised cluster separation |

---

## 💡 Key Insights & PCA vs. LDA Comparison

```
PCA (Unsupervised)                          LDA (Supervised)
───────────────────                         ────────────────
• Ignores class labels                      • Utilizes class labels
• Maximizes overall data variance           • Maximizes between-class variance / minimizes within-class variance
• Optimal for compression & denoising       • Optimal for feature projection prior to classification
• Preserves global data spread              • Enforces tight, well-separated class clusters
```

- **SVM Regularization**: Optimal $C$ strikes the ideal balance between boundary margin width and classification slack penalties.
- **PCA Loadings**: Features like Flavanoids, Total Phenols, and OD280/OD315 contribute heavily to the first principal component, capturing the primary chemical variation across wines.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
Open and run [`ML-LAB9.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB9/ML-LAB9.ipynb) in Jupyter Notebook or VS Code.
