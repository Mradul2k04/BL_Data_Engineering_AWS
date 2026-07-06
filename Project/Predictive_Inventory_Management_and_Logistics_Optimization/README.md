# Predictive Inventory Management and Logistics Optimization

This project aims to optimize supply chain operations through predictive modeling. It uses generated synthetic data to forecast logistical transport costs and assess the risk of stock shortages across various warehouses, products, and suppliers.

## Overview

The project is structured around two main components:
1. **Data Generation (`data_generation.py`)**: A script that uses the `Faker` library to generate realistic, synthetic supply chain data, capturing details such as warehouses, products, stock levels, reorder levels, suppliers, and transport costs.
2. **Predictive Modeling (`notebook_1.ipynb`)**: A Jupyter Notebook that explores the generated dataset, handles missing data, extracts features, and builds predictive models:
   - **Linear Regression**: Predicts the continuous `Transport Cost` based on various features.
   - **Random Forest Classifier**: Classifies and predicts `Stock Shortage Risk` (whether current stock is below the reorder level).

## Requirements

Ensure you have Python 3.x installed. Required packages include:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `Faker`

You can install the dependencies via pip:
```bash
pip install -r requirements.txt
```
*(Note: If `matplotlib`, `seaborn`, or `scikit-learn` are missing, please run `pip install matplotlib seaborn scikit-learn` manually).*

## Usage

### 1. Generating Data
Run the data generation script to create a fresh `predictive_inventory_dataset.csv` file with 1,000 randomized supply chain records:
```bash
python data_generation.py
```

### 2. Exploring and Modeling
Launch Jupyter Notebook to interact with `notebook_1.ipynb`:
```bash
jupyter notebook notebook_1.ipynb
```
The notebook executes the following pipeline:
- **Exploratory Data Analysis (EDA)**: Visualizes distributions and correlations in the dataset.
- **Data Cleaning**: Imputes missing stock level data using median values.
- **Feature Engineering**: Extracts temporal features from dates and generates a classification target for stock shortages.
- **Modeling & Evaluation**: Fits a Linear Regression model for transport costs and a Random Forest Classifier for stock shortage risks, then evaluates performance using metrics such as Accuracy, Precision, Recall, F1 Score, and MAE.

## License
MIT License
