# ML Lab — Trimester 4

This repository contains the coursework and experiments for the Machine Learning lab (Trimester 4). It includes datasets and a Jupyter notebook demonstrating data exploration and model work for the class lab exercises.

## Repository structure

- `dataset/` — CSV data files used in the lab:
	- `city_day.csv` — daily city-level observations (description below).
	- `crop_production.csv` — historical crop production data.
- `ML-LAB1/ML_LAB1.ipynb` — primary Jupyter notebook with analysis, visualizations, and model exercises.

## Datasets

- `city_day.csv`: daily measurements aggregated by city. Use this dataset for time-series exploration, aggregation, and visualization exercises.
- `crop_production.csv`: contains crop production metrics (year, crop type, production values). Useful for regression and trend analysis tasks.

If you need more details about columns, open the CSV files directly or inspect the notebook cells where the datasets are loaded and described.

## Requirements

- Python 3.8+ (recommended)
- Jupyter or JupyterLab
- Common data science packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

You can install the basic requirements with pip:

```bash
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scikit-learn notebook
```

## How to run

1. Clone or pull this repository.
2. Install the dependencies (see Requirements).
3. Launch Jupyter in the repository root:

```bash
jupyter notebook
```

4. Open `ML-LAB1/ML_LAB1.ipynb` and run the cells.

## Notes and tips

- The notebook includes data loading and example preprocessing steps; adapt the code to your experiments.
- If datasets are large, consider sampling or using chunked reads with `pandas.read_csv(..., chunksize=...)`.

## Contributing

- This repository is intended for personal coursework. If you wish to share improvements or corrections, feel free to open a pull request or contact the owner.

## License

- This project is for educational use. No explicit license is provided — contact the owner for reuse permissions.

---

I