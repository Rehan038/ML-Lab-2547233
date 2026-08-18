# Machine Learning Lab 8: Naïve Bayes Classification & Model Comparison

## 📌 Overview
This lab implements and evaluates the probabilistic **Categorical Naïve Bayes** classification algorithm on discrete tabular data (`lab8.csv`). It covers data preprocessing, categorical label encoding, prior and posterior probability estimation, single-sample inference, and a comparative performance benchmark against **Decision Trees**, **Logistic Regression**, and **Support Vector Classifiers (SVC)**.

---

## 🎯 Objectives
- **Categorical Feature Preprocessing**:
  - Transform discrete categorical survey/tabular columns into numerical indices using `LabelEncoder`.
- **Naïve Bayes Formulation**:
  - Understand the Bayes' Theorem under conditional feature independence:
    $$P(Y \mid X_1, X_2, \dots, X_n) \propto P(Y) \prod_{i=1}^{n} P(X_i \mid Y)$$
  - Train `CategoricalNB` to model prior probabilities $P(Y)$ and class-conditional probabilities $P(X_i \mid Y)$ with Laplace smoothing.
- **Single-Sample Inference**:
  - Perform real-time class prediction and posterior probability querying for hypothetical individual test vectors.
- **Multi-Model Benchmark**:
  - Benchmark Naïve Bayes against:
    1. **Decision Tree Classifier** (`criterion='gini'`)
    2. **Logistic Regression**
    3. **Support Vector Machine Classifier** (`SVC(kernel='linear')`)
  - Evaluate and compare models using Accuracy, Confusion Matrix, and Classification Reports.

---

## 📊 Dataset Description
- **`lab8.csv`**:
  - Tabular multi-attribute dataset containing discrete categorical survey features.
  - Multi-class target variable requiring discrete probability distribution estimation.

---

## 🔬 Lab Workflow & Key Experiments

| Phase | Description | Key Methods / Modules |
| :--- | :--- | :--- |
| **Phase 1: Preprocessing** | Loading data, handling missing entries, label encoding discrete variables | `pandas.read_csv()`, `LabelEncoder()` |
| **Phase 2: Partitioning** | Splitting dataset into training and testing partitions | `train_test_split(test_size=0.2, random_state=42)` |
| **Phase 3: Model Training** | Fitting Categorical Naïve Bayes with Laplace smoothing | `sklearn.naive_bayes.CategoricalNB()` |
| **Phase 4: Single Inference** | Querying posterior class likelihoods for a single test input sample | `.predict()`, `.predict_proba()` |
| **Phase 5: Benchmark** | Comparing Naïve Bayes, Decision Tree, Logistic Regression, and Support Vector Classifier | `accuracy_score()`, `classification_report()`, `confusion_matrix()` |

---

## 📈 Benchmark & Key Insights

| Algorithm | Strengths | Performance Summary |
| :--- | :--- | :--- |
| **Categorical Naïve Bayes** | Extremely fast training, handles categorical priors naturally, strong with small data | **Top Performer (~80% Accuracy)** |
| **Decision Tree** | Captures non-linear feature interactions without independence assumptions | **Top Performer (~80% Accuracy)** |
| **Logistic Regression** | Linear probability calibration; requires feature dummy expansion for best fit | Moderate Performance |
| **Support Vector Classifier** | Maximizes hyperplane margin | Moderate Performance |

### 💡 Key Takeaways:
- **Strong Categorical Suitability**: For discrete categorical data with independent indicators, Naïve Bayes performs remarkably well despite its "naïve" conditional independence assumption.
- **Inference Speed**: CategoricalNB provides instantaneous probability lookups without iterative optimization cycles during prediction time.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
Open and run [`ML-LAB8.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB8/ML-LAB8.ipynb) in Jupyter Notebook or VS Code.
