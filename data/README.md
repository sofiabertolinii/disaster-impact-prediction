# Data

This directory contains all processed datasets used throughout the project, as well as the scripts responsible for the **feature engineering** stage.

The datasets are organized according to the iterative Data Science workflow proposed in this project, allowing the reproduction of all experimental configurations.

The original dataset can be downloaded in the official Brazilian government website.

```text
data/
│
├── dataset_v1/
├── dataset_v2/
├── dataset_v3/
├── feature_engineering/
└── README.md
```

---

## Directory Structure

### `dataset_v1`

The first version of the dataset.

In this version, hydrographic basin information is represented using a **power-of-two encoding**, allowing multiple basin memberships to be stored in a single numerical feature.

This dataset version achieved the best overall performance in the experiments.

---

### `dataset_v2`

The second version of the dataset.

Each hydrographic basin is represented by an individual binary feature indicating whether a municipality belongs to that basin.

This representation was created to evaluate an alternative spatial encoding strategy.

---

### `dataset_v3`

The third version of the dataset.

Instead of binary membership, hydrographic basins are represented by the **percentage of the municipality's area** located within each basin, providing a more detailed spatial representation.

---

### `feature_engineering`

This directory contains the scripts responsible for constructing the datasets used in this project.

The feature engineering pipeline includes:

- Data cleaning and preprocessing
- Integration of multiple public datasets
- Feature creation
- Hydrographic basin encoding
- Target variable generation
- Construction of the three final dataset versions

The main engineered features include:

- Year
- Month
- Season
- Municipal Area
- Population
- Hydrographic Basin
- Niño 3.4
- Climate Event
- HDI-M
- Vegetation Cover

The following target variables were also created:

- Human Damage Percentage Classification
- Material Damage Per Capita Classification
- Public Loss Per Capita Classification
- Private Loss Per Capita Classification

---

## Data Sources

The primary data source used in this project is the **Digital Atlas of Natural Disasters in Brazil**, published by the Brazilian Ministry of Integration and Regional Development (MIDR).

The original dataset was enriched with additional information from official public sources, including:

- Brazilian Institute of Geography and Statistics (IBGE)
- Oceanic Niño Index (ONI)
- Brazilian Atlas of Human Development
- Vegetation cover datasets
- Hydrographic basin data

---

## Notes

The three dataset versions correspond to different feature engineering strategies evaluated throughout the experiments. Their purpose is to analyze how different representations of hydrographic basin information influence the predictive performance of the Machine Learning models.