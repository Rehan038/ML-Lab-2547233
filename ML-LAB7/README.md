# Machine Learning Lab 7: Decision Tree Classification, Pruning, & Hyperparameter Tuning

## 📌 Overview
This lab provides a comprehensive exploration of **Decision Tree Classifiers** on Fisher's **Iris Flower Dataset**. It covers tree construction, tree visualization, splitting criteria comparison (Gini Impurity vs. Information Gain / Entropy), overfitting analysis via depth constraints, and pre-pruning regularization techniques.

---

## 🎯 Objectives
- **Data Exploration & Visual Inspection**:
  - Load the multi-class Iris dataset (150 samples, 3 classes: Setosa, Versicolor, Virginica).
  - Analyze feature distributions across sepal and petal measurements.
- **Tree Construction & Feature Split Visualizations**:
  - Fit `DecisionTreeClassifier` and generate interpretable decision tree diagrams using `sklearn.tree.plot_tree`.
  - Analyze how root and internal nodes prioritize features based on maximal Information Gain (e.g., Petal Length as the primary discriminative feature).
- **Splitting Criteria Comparison**:
  - Compare **Gini Impurity**:
    $$I_G(p) = 1 - \sum_{i=1}^{C} p_i^2$$
  - With **Information Gain / Entropy**:
    $$H(S) = - \sum_{i=1}^{C} p_i \log_2(p_i)$$
- **Overfitting & Tree Complexity Analysis**:
  - Analyze the effect of maximum tree depth (`max_depth = 1, 2, 3, None`).
  - Identify underfitting (shallow depth, high bias) vs. overfitting (unconstrained depth, high variance, memorizing noise).
- **Pre-Pruning Regularization**:
  - Study the regularization effect of `min_samples_split` (minimum samples required to split an internal node).
  - Study `min_samples_leaf` (minimum samples required at a leaf node).
- **Hyperparameter Optimization**:
  - Determine optimal parameters combining balanced tree depth, leaf constraints, and high generalization accuracy.

---

## 📊 Dataset Description
- **Fisher's Iris Dataset**:
  - 150 instances (50 per class).
  - 4 continuous input features: Sepal Length, Sepal Width, Petal Length, Petal Width.
  - 3 target classes: *Iris Setosa* (0), *Iris Versicolor* (1), *Iris Virginica* (2).

---

## 🔬 Lab Tasks & Experiments

| Task | Focus Area | Observations / Techniques |
| :--- | :--- | :--- |
| **Task 1 & 2** | Dataset Exploration & Preparation | 80:20 Stratified train-test split |
| **Task 3 & 4** | Building & Visualizing Decision Tree | `plot_tree()`, observing root split on Petal Length |
| **Task 5** | Gini Impurity vs. Entropy Criterion | Both achieve top-tier test accuracy; Gini is computationally faster |
| **Task 6** | Maximum Tree Depth (`max_depth`) | `max_depth=1` underfits; `max_depth=3` achieves optimal generalization; unconstrained depth risks overfitting |
| **Task 7** | Minimum Samples Split (`min_samples_split`)| Larger values prevent minor branch splits on outlier clusters |
| **Task 8** | Minimum Samples Leaf (`min_samples_leaf`) | Enforces smoother boundaries by forbidding single-instance leaf nodes |
| **Task 9** | Hyperparameter Tuning & Pruning | Configured an optimal pruned tree maintaining 100% test accuracy with simplified structure |

---

## 💡 Key Conceptual Insights
1. **Feature Dominance**: Petal measurements provide almost complete linear separability for *Iris Setosa*, making them the universal choice for the root decision split.
2. **Gini vs. Entropy**: In practice, Gini Impurity and Entropy yield nearly identical decision boundaries, but Gini avoids logarithmic computations, offering better training efficiency.
3. **Regularization through Pruning**: Setting `max_depth`, `min_samples_split`, and `min_samples_leaf` effectively acts as pre-pruning, preventing the tree from growing complex leaves tailored to training noise.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```
Open and run [`ML-LAB7.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB7/ML-LAB7.ipynb) in Jupyter Notebook or VS Code.
