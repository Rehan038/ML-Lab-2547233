# Machine Learning Lab 5: Linear Regression with Gradient Descent Optimization

## 📌 Overview
This lab implements **Linear Regression through Gradient Descent Optimization** from mathematical first principles on the real-world **Student Performance Dataset**. The experiment focuses on loss minimization, learning rate dynamics, convergence tracking, and regression error evaluation.

---

## 🎯 Objectives
- **Data Preprocessing & Encoding**:
  - Load student demographic, social, and academic indicators (`student-mat.csv`).
  - Convert multi-category attributes into numerical matrices using One-Hot Encoding (`pd.get_dummies(drop_first=True)`).
  - Apply `StandardScaler` to bring all continuous feature columns to unit variance and zero mean.
- **Custom Gradient Descent Implementation from Scratch**:
  - Formulate the Mean Squared Error (MSE) cost function:
    $$J(\mathbf{w}, b) = \frac{1}{2m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right)^2 = \frac{1}{2m} \sum_{i=1}^{m} \left( \mathbf{w}^T \mathbf{x}^{(i)} + b - y^{(i)} \right)^2$$
  - Derive and iteratively compute weight and bias gradient updates:
    $$\frac{\partial J}{\partial \mathbf{w}} = \frac{1}{m} \mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y}), \quad \frac{\partial J}{\partial b} = \frac{1}{m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)})$$
    $$\mathbf{w} := \mathbf{w} - \alpha \frac{\partial J}{\partial \mathbf{w}}, \quad b := b - \alpha \frac{\partial J}{\partial b}$$
- **Hyperparameter Tuning & Learning Rate Analysis**:
  - Experiment across different learning rates ($\alpha \in \{0.0001, 0.001, 0.01, 0.1\}$).
  - Plot and analyze **Cost vs. Iterations** curves to observe fast convergence, slow convergence, and potential divergence/overshooting.
- **Model Evaluation**:
  - Quantify final prediction performance on unseen test data using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and $R^2$ score.

---

## 📊 Dataset Description
- **Student Performance Data (`student-mat.csv`)**:
  - 395 records and 33 features capturing student grades, demographic attributes, social background, family relationships, study time, absences, and academic history.
  - Predictors: Continuous and one-hot encoded categorical attributes.
  - Target: Final academic grade ($G3$).

---

## 🔬 Lab Workflow & Key Steps

| Step | Description | Technical Implementation |
| :--- | :--- | :--- |
| **Step 1: Dataset Exploration** | Inspection of data types, missing values, duplicates, and statistical distribution | `pandas.info()`, `.describe()` |
| **Step 2: Preprocessing & Encoding** | Categorical conversion via One-Hot Encoding and feature matrix scaling | `pd.get_dummies()`, `StandardScaler()` |
| **Step 3: Train-Test Partitioning** | Stratified split into 70% training and 30% testing subsets | `train_test_split(test_size=0.3, random_state=42)` |
| **Step 4: Vectorized Gradient Descent** | Custom Python implementation of batch gradient descent with loss history logging | Vectorized NumPy array operations |
| **Step 5: Learning Rate Experiments** | Comparative analysis across $\alpha$ values to track convergence behavior | Iterative loss logging across 1,000+ epochs |
| **Step 6: Loss Convergence Visualization** | Plotting $J(\mathbf{w}, b)$ decay curves across training iterations | `matplotlib.pyplot.plot(iterations, cost)` |
| **Step 7: Performance Evaluation** | Evaluating test set residuals and goodness of fit | MAE, MSE, RMSE, $R^2$ Score |

---

## 💡 Key Observations
- **Learning Rate Sensitivity**:
  - Overly small learning rates ($\alpha = 0.0001$) result in very slow convergence requiring tens of thousands of steps.
  - An optimal learning rate ($\alpha = 0.01 - 0.05$) ensures smooth, monotonic loss decrease reaching steady-state convergence within a few hundred iterations.
  - Excessively large rates can cause gradient oscillations or divergence.
- **Convergence Verification**: The cost function asymptotically stabilizes as gradients approach zero ($\nabla J \approx 0$), proving successful parameter optimization.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy pandas matplotlib scikit-learn
```
Open and run [`ML-LAB5.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB5/ML-LAB5.ipynb) in Jupyter Notebook or VS Code.
