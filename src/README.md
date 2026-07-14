# Source Code

This directory contains the source code responsible for executing the complete Machine Learning workflow, from data loading to model evaluation.

```text
src/
│
├── data_loader.py
├── models.py
├── pipeline.py
├── main.py
└── README.md
```

---

## File Structure

### `main.py`

Entry point of the project.

This script is responsible for configuring the experiment and executing the complete Machine Learning pipeline. It coordinates the interaction between the data loading, model selection, and evaluation modules.

---

### `data_loader.py`

Handles dataset loading and preprocessing.

Its main responsibilities include:

- Loading the selected dataset version;
- Applying the preprocessing required for each experiment;
- Filtering the data according to the selected test configuration;
- Splitting features and target variables;
- Returning data ready for model training and evaluation.

---

### `models.py`

Defines and initializes the Machine Learning models used throughout the experiments.

The supported algorithms are:

- Decision Tree
- Random Forest
- Logistic Regression
- Multi-Layer Perceptron (MLP)
- XGBoost

This module centralizes model creation, making it easier to compare different algorithms while keeping the pipeline consistent.

---

### `pipeline.py`

Implements the experimental workflow.

Its responsibilities include:

- Training the selected model;
- Performing 3-fold cross-validation;
- Computing evaluation metrics;
- Comparing model performance across different datasets and experimental configurations;
- Returning the results generated during the experiments.

