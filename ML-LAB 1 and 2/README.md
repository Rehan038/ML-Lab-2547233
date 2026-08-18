# Machine Learning Lab 1 & 2: Exploratory Data Analysis & Air Quality - Crop Production Case Study

## 📌 Overview
This lab repository contains exploratory data analysis (EDA), data cleaning, statistical evaluation, and cross-dataset synthesis examining air quality trends across Indian cities and their potential correlation with agricultural crop production.

---

## 🎯 Objectives
- **Data Exploration & Profiling**: Inspect structural attributes, feature data types, missing value distributions, and summary statistics across large-scale tabular datasets.
- **Data Cleaning & Preprocessing**:
  - Impute missing pollutant concentrations using column medians to ensure robustness against high-value outliers.
  - Impute missing crop production values using state-wise median values.
  - Standardize text columns (city names, state names) by converting to lowercase and stripping whitespaces.
- **Outlier Detection & Treatment**:
  - Identify extreme Air Quality Index (AQI) readings using the Interquartile Range (IQR) method.
  - Apply outlier capping (Winsorization) using upper and lower fences:
    $$\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR}, \quad \text{Upper Fence} = Q_3 + 1.5 \times \text{IQR}$$
- **Time-Series & Seasonality Analysis**:
  - Aggregate annual AQI trends across years to detect historical pollution dips and spikes.
  - Conduct month-wise seasonal checks via boxplots to assess post-monsoon and winter smog spikes (Oct–Dec).
- **Multi-Dataset Merging & Hypothesis Testing**:
  - Standardize geographic identifiers and temporal keys to merge urban air quality records with district/state crop yields.
  - Compute Pearson correlation coefficient and regression metrics to evaluate whether state-level AQI significantly correlates with total agricultural output.

---

## 📊 Datasets Used
1. **`city_day.csv`**: Daily environmental and pollutant records (PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3, Benzene, Toluene, Xylene, AQI, AQI Bucket) across major Indian cities.
2. **`crop_production.csv`**: Historical agricultural statistics across India featuring state name, district name, crop year, season, crop type, cultivated area, and production output.

---

## 🔬 Key Tasks & Workflow

| Task | Description | Techniques / Tools |
| :--- | :--- | :--- |
| **Task 1: Data Understanding** | Initial dataset inspection, shape verification, null checks, duplicate checks, statistical summary | `pandas.DataFrame.info()`, `.describe()`, `.isnull().sum()` |
| **Task 2: Missing Value Handling** | Median imputation for pollutant concentrations and state-grouped median for crop production | `pandas.fillna()`, `groupby().transform('median')` |
| **Task 3: Text Standardization** | String cleaning and normalization for geographic consistency across datasets | `.str.lower().str.strip()` |
| **Task 4: Distribution Analysis** | Histogram and KDE visualization of right-skewed AQI measurements | `seaborn.histplot()`, `matplotlib.pyplot` |
| **Task 5: Outlier Capping** | IQR-based outlier capping and before/after comparison plots | `numpy.clip()`, `seaborn.boxplot()` |
| **Task 6: Annual Trend Analysis** | Time-series trend line plotting highlighting peak and low pollution years | `seaborn.lineplot()`, annual aggregation |
| **Task 7: Seasonality Check** | Monthly AQI distribution analysis to isolate winter/harvest season impact | `seaborn.boxplot()`, month grouping |
| **Task 8: Dataset Integration** | Mapping cities to states and aggregating annual means for cross-domain merging | `pandas.merge()`, inner join on `State_Name` and `Year` |
| **Task 9: Impact & Correlation Study**| Pearson correlation analysis between statewide AQI and crop production volume | `scipy.stats.pearsonr`, scatter plots |

---

## 💡 Key Findings & Insights
- **Pollution Seasonality**: Air quality deteriorates drastically during October–December (harvesting and winter inversion season).
- **State-Level Correlation**: While seasonal smog correlates with the post-harvest period, statewide aggregate crop production and mean annual AQI show a weak direct linear correlation ($R^2 \approx 4.6\%$), indicating agricultural yields are predominantly governed by irrigation, rainfall, soil fertility, and farming technology rather than ambient urban AQI alone.

---

## 🛠️ Requirements & Setup
```bash
pip install numpy pandas matplotlib seaborn scipy
```
Open and run [`ML_LAB1 and 2.ipynb`](file:///c:/Users/Rehan/OneDrive/Desktop/Trimester4/ML%20Lab/ML-LAB%201%20and%202/ML_LAB1%20and%202.ipynb) in Jupyter Notebook, JupyterLab, or VS Code.
