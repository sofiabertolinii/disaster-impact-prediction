# Natural Disaster Impact Prediction using Machine Learning

A Data Science workflow for predicting the social, economic, and material impacts of natural disasters in Rio Grande do Sul, Brazil.

---

## Overview

Natural disasters have become increasingly frequent and severe, making impact prediction an important tool for disaster preparedness and decision-making.

This project proposes an iterative Data Science workflow that integrates historical disaster records with climatic, geographic, demographic, and socioeconomic information to predict disaster impacts using Machine Learning.

The workflow includes:

- Data acquisition
- Data preprocessing
- Feature engineering
- Dataset construction
- Model training
- Model evaluation
- Feature importance analysis

Five Machine Learning algorithms were evaluated:

- Decision Tree
- Random Forest
- Logistic Regression
- Multi-Layer Perceptron (MLP)
- XGBoost

---

## Main Dataset

The primary data source is the **Digital Atlas of Natural Disasters in Brazil (Atlas Digital de Desastres no Brasil)**, published by the Brazilian Ministry of Integration and Regional Development.

The Atlas contains more than **70,000 records** describing natural disasters that occurred between **1991 and 2025**, including:

- disaster type
- affected municipality
- event date
- human impacts
- material damages
- public losses
- private losses

The original dataset was enriched with additional information obtained from official Brazilian data sources, including:

- Instituto Brasileiro de Geografia e Estatpistica (IBGE) population data
- Municipal area
- Hydrographic basins
- Oceanic Niño Index (ONI)
- Climate event classification (El Niño / La Niña / Neutral)
- Municipal Human Development Index (HDI-M)
- Vegetation cover

---

## Feature Engineering

Several new features were created to improve model performance, including:

- Year
- Month
- Season
- Municipal area
- Population
- Hydrographic basin representation
- Nino 3.4 index
- Climate event
- HDI-M
- Vegetation cover

Three different hydrographic basin representations were evaluated:

1. Power-of-two encoding
2. Binary encoding
3. Percentage of municipal area inside each basin

Target variables were also engineered by transforming disaster impacts into classification problems:

- Human Damage Percentage Classification
- Material Damage Per Capita Classification
- Public Loss Per Capita Classification
- Private Loss Per Capita Classification

---

## Experimental Setup

Three dataset versions were evaluated together with three experimental configurations.

### Dataset Versions

- Version 1 — Power-of-two basin encoding
- Version 2 — Binary basin encoding
- Version 3 — Percentage of municipal area in each basin

### Test Configurations

**Test 1**

- Five classes
- Class 0 represents no impact
- Classes 1–4 correspond to quartiles of non-zero values

**Test 2**

- Removes records with no impact
- Four severity classes

**Test 3**

- Binary classification
- Impact vs. No Impact

---

## Models

The following Machine Learning models were evaluated:

- Decision Tree
- Random Forest
- Logistic Regression
- Multi-Layer Perceptron
- XGBoost

Model evaluation was performed using:

- Accuracy
- Precision
- F1-score
- Balanced Accuracy

All experiments used **3-fold Cross Validation**.

---

## Results

The experiments showed that:

- XGBoost achieved the best overall performance.
- Decision Trees produced competitive results while remaining highly interpretable.
- Dataset Version 1 consistently outperformed the other dataset representations.
- Binary classification (Test 3) achieved the highest accuracy, reaching approximately **80%**.

Feature importance analysis using SHAP indicated that temporal and climatic variables were the strongest predictors, especially:

- Register Year
- Nino 3.4 Ocean Temperature
- Register Month
- 
---

## Installation

Clone the repository:

```bash
git clone this repository
```

Move into the project directory

Install all required dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains all Python packages required to reproduce the preprocessing pipeline, train the models, and execute the experiments.

---

## Requirements

This project was developed using **Python 3.12**.

Main libraries include:

- pandas
- numpy
- scikit-learn
- xgboost

Complete dependency versions are available in `requirements.txt`.

---

## Reproducing the Experiments

1. Download the required datasets.
2. Place them inside the appropriate dataset directory.
3. Run the preprocessing scripts.
4. Execute the desired model.
5. Evaluate the generated metrics.

The experiments reproduce the workflow described in the accompanying paper.

---

## Citation

If you use this repository in your research, please cite:

> *Uma Análise Comparativa de Algoritmos de Aprendizado de Máquina no Estado do Rio Grande do Sul*, ERAMIA RS 2026

---

## Future Work

Possible future improvements include:

- Integration of rainfall accumulation data
- River network modeling using Graph Neural Networks
- Additional meteorological variables
- Soil and altitude information
- Spatio-temporal prediction models
- Explainable AI methods

---
