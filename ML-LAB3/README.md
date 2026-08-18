# Machine Learning Lab 3: Simple Linear Regression & Ordinary Least Squares (OLS)

## 📌 Overview
This lab covers the fundamentals of **Simple Linear Regression**, exploring the mathematical derivation and practical implementation of Ordinary Least Squares (OLS) both from scratch using closed-form analytical formulas and using `scikit-learn`. The study evaluates academic performance indicators from student survey data.

---

## 🎯 Objectives
- **Data Cleaning & Regex Extraction**:
  - Clean real-world survey responses by removing units, special characters (`%`, `+`, `LPA`), and converting messy string entries to clean numerical data types.
  - Filter domain-specific invalid records (e.g., GPA > 4.0 or anomalous exam percentages).
- **Simple Linear Regression Modeling**:
  - Model relationship between **Continuous Assessment (CIA) Percentage** and **GPA**.
  - Model relationship between **Attendance Percentage** and **GPA**.
- **Mathematical Derivation & Closed-Form OLS**:
  - Compute slope ($\beta_1$) and intercept ($\beta_0$) manually:
    $$\beta_1 = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2}, \quad \beta_0 = \bar{Y} - \beta_1 \bar{X}$$
  - Prove mathematical equivalence between custom manual formulas and Scikit-Learn's `LinearRegression` implementation.
- **Model Evaluation**:
  - Compute Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Coefficient of Determination ($R^2$).
- **Model Persistence**:
  - Serialize model weights and artifacts using Python's `pickle` library for reusable inference.

---

## 📊 Dataset Description
- **`student_survey.csv`**: Contains student responses capturing:
  - Input Predictors: CIA Marks / Continuous Assessment Percentage, Class Attendance Percentage, Study Hours.
  - Target Variable: Cumulative Grade Point Average (**GPA**).

---

## 🔬 Lab Breakdown & Experiments

| Part / Experiment | Focus Area | Key Metrics / Methods |
| :--- | :--- | :--- |
| **Part A: Preprocessing** | Dropping non-predictive metadata (timestamps, emails), string normalization, regex extraction, outlier trimming | `re.sub()`, `pd.to_numeric()`, sanity boundary checks |
| **Part B: Experiment 1** | Simple Linear Regression: $\text{CIA Percentage} \rightarrow \text{GPA}$ using Scikit-Learn | `LinearRegression().fit()`, MAE, MSE, $R^2$ |
| **Part B: Experiment 2** | Simple Linear Regression: $\text{Attendance Percentage} \rightarrow \text{GPA}$ using Scikit-Learn | `LinearRegression().fit()`, MAE, MSE, $R^2$ |
| **Part C: Manual OLS** | Closed-form parameter estimation ($\beta_0, \beta_1$) for both experiments and exact parity validation | Custom NumPy covariance/variance computation |
| **Part D: Model Serialization**| Persisting trained coefficients and model objects to disk for inference | `pickle.dump()`, `pickle.load()` |

---

## 💡 Key Takeaways
- **Positive Relationship**: Both continuous assessment marks and classroom attendance exhibit positive slopes relative to overall GPA.
- **Formulas Equivalence**: Predictions and error metrics computed via the manual OLS formula matched `sklearn.linear_model.LinearRegression` to machine precision ($10^{-15}$).
- **Model Persistence**: Serializing trained parameters using `pickle` enables lightweight deployment without model re-training.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy pandas matplotlib scikit-learn
```
Open and run [`ML-LAB3.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB3/ML-LAB3.ipynb) in Jupyter Notebook or VS Code.
