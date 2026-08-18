# Machine Learning Laboratory (Trimester 4)

Welcome to the **Machine Learning Laboratory** repository. This repository contains complete, well-documented Jupyter notebook implementations, exploratory analyses, empirical studies, and mathematical formulations covering foundational and advanced machine learning algorithms.

---

## 📂 Repository Structure & Lab Index

```
ML Lab/
├── ML-LAB 1 and 2/    # EDA, Missing Value Imputation, Outliers, AQI-Crop Case Study
├── ML-LAB3/           # Simple Linear Regression & Closed-Form OLS
├── ML-LAB4/           # K-Nearest Neighbors (KNN) & Classification vs. Regression
├── ML-LAB5/           # Linear Regression via Vectorized Gradient Descent
├── ML-LAB6/           # Benchmark: Logistic Regression vs. K-Nearest Neighbors (KNN)
├── ML-LAB7/           # Decision Tree Classification, Pruning, & Hyperparameter Tuning
├── ML-LAB8/           # Categorical Naïve Bayes & Multi-Model Classification Benchmark
├── ML-LAB9/           # Support Vector Machines (SVM), PCA, & LDA Dimensionality Reduction
├── ML-LAB10/          # Multi-Layer Perceptrons (MLP) & Solving Non-Linear XOR Problem
└── README.md          # Repository Master Index & Overview
```

---

## 🔬 Summary of Laboratory Modules

| Lab Module | Primary Focus & Algorithms | Key Concepts & Datasets | Detailed Documentation |
| :--- | :--- | :--- | :---: |
| **[ML-LAB 1 and 2](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB%201%20and%202)** | **Exploratory Data Analysis & Case Study** | Data cleaning, median imputation, IQR outlier capping, time-series trends, seasonal pollution analysis, cross-domain dataset merging (`city_day.csv` & `crop_production.csv`). | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB%201%20and%202/README.md) |
| **[ML-LAB3](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB3)** | **Simple Linear Regression & OLS** | Closed-form analytical OLS parameter calculation vs. `scikit-learn`, regex data cleaning, $R^2$/MSE evaluation, and model persistence via `pickle`. | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB3/README.md) |
| **[ML-LAB4](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB4)** | **$K$-Nearest Neighbors (KNN)** | Feature standardization (`StandardScaler`), train-test split stability, heuristic $K=\sqrt{n}$, cross-validation pipeline, decision boundaries, classification vs. regression framing. | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB4/README.md) |
| **[ML-LAB5](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB5)** | **Linear Regression via Gradient Descent** | First-principles vectorized batch Gradient Descent implementation, learning rate ($\alpha$) optimization, cost function convergence curves ($J(\mathbf{w},b)$ vs. iterations). | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB5/README.md) |
| **[ML-LAB6](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB6)** | **Logistic Regression vs. KNN Benchmark** | Direct comparative performance benchmark on cancer diagnosis, precision-recall trade-offs, clinical False Negative cost analysis, and high-dimensional distance behavior. | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB6/README.md) |
| **[ML-LAB7](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB7)** | **Decision Trees & Hyperparameter Pruning** | Tree construction & graphical visualization (`plot_tree`), Gini Impurity vs. Information Gain (Entropy), depth constraints (`max_depth`), pre-pruning regularization (`min_samples_split`, `min_samples_leaf`). | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB7/README.md) |
| **[ML-LAB8](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB8)** | **Naïve Bayes & Multi-Classifier Benchmark** | Categorical Naïve Bayes with Laplace smoothing, prior/posterior distribution estimation, single-sample inference, and multi-model benchmark vs. Decision Tree, Logistic Regression, and SVC. | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB8/README.md) |
| **[ML-LAB9](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB9)** | **SVM, PCA, & LDA Dimensionality Reduction** | Support Vector Classifiers with margin parameter tuning (`GridSearchCV`), unsupervised PCA variance analysis & loadings, supervised LDA cluster maximization, and 2D projection comparisons. | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB9/README.md) |
| **[ML-LAB10](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB10)** | **Multi-Layer Perceptrons & Non-Linear XOR** | Solving linear inseparability via deep forward networks, hidden layer transformations, Keras Sequential API and low-level TensorFlow (`tf.GradientTape`) backpropagation, decision boundary mesh plots. | [README](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB10/README.md) |

---

## 🛠️ Environment & Prerequisites

To execute and reproduce all lab notebooks, ensure Python 3.8+ is installed and install the required machine learning and data science packages:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy tensorflow
```

---

## 🚀 Getting Started

1. **Clone or Navigate to the Workspace**:
   ```bash
   cd "ML Lab"
   ```
2. **Launch Jupyter Lab / Notebook**:
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```
3. **Open Any Module**: Navigate into any specific lab folder (e.g. `ML-LAB5/`) and open its `.ipynb` notebook file to view, execute, or experiment with the code and visualizations.
