# 🧠 EEG-Based Disease Classification

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Multi-class classification of neurological disorders using EEG electrode readings and demographic data.

## Overview

This repository implements machine learning classifiers to predict neurological disorders from 32-channel EEG data combined with participant demographics (age, sex, education, IQ, EQ). The pipeline includes preprocessing, feature engineering, model training, and evaluation.

## Dataset

The dataset contains:
- **Features**: 32 EEG electrode readings, age, sex, education level, IQ, EQ
- **Target**: Disorder/diagnosis classification
- **Format**: CSV with columns for participant demographics and `EEG_Electrode_{1-32}`

## Installation

```bash
git clone https://github.com/yourusername/eeg-classification.git
cd eeg-classification
pip install -r requirements.txt
```

### Dependencies

```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

## Usage

### Preprocessing

```python
from src.preprocessing import preprocess_data

# Load and preprocess
X_train, X_test, y_train, y_test = preprocess_data('data/eeg_dataset.csv')
```

The preprocessing pipeline handles:
1. Missing value imputation
2. Categorical encoding (sex, education)
3. Feature scaling (StandardScaler on continuous variables)
4. Train-test split with stratification

### Training

```python
from src.train import train_models

# Train multiple classifiers
models = train_models(X_train, y_train)
```

Implemented models:
- Random Forest
- Support Vector Machine (RBF kernel)
- Multi-layer Perceptron

### Evaluation

```python
from src.evaluate import evaluate_models

# Generate metrics and visualizations
results = evaluate_models(models, X_test, y_test)
```

Outputs:
- Confusion matrices
- Classification reports (precision, recall, F1-score)
- Feature importance plots
- EEG pattern visualizations by disorder

## Pipeline

```
Raw Data
   ↓
Missing Value Handling
   ↓
Categorical Encoding
   ↓
Feature Scaling
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Evaluation & Visualization
```

## Results

| Model | Accuracy | F1-Score (Weighted) |
|-------|----------|---------------------|
| Random Forest | TBD | TBD |
| SVM | TBD | TBD |
| Neural Network | TBD | TBD |

## Project Structure

```
eeg-classification/
├── data/
│   └── eeg_dataset.csv
├── src/
│   ├── preprocessing.py      # Data cleaning and feature engineering
│   ├── train.py              # Model training
│   └── evaluate.py           # Metrics and visualization
├── notebooks/
│   └── exploration.ipynb     # Exploratory data analysis
├── models/
│   └── saved_models/         # Serialized trained models
├── results/
│   ├── figures/              # Generated plots
│   └── metrics/              # Performance metrics
├── requirements.txt
├── README.md
└── LICENSE
```

## Key Implementation Details

### Feature Engineering

```python
# Statistical aggregations across electrodes
df['EEG_mean'] = df.filter(like='EEG_Electrode').mean(axis=1)
df['EEG_std'] = df.filter(like='EEG_Electrode').std(axis=1)
df['EEG_max'] = df.filter(like='EEG_Electrode').max(axis=1)
```

### Handling Class Imbalance

```python
# Use class weighting in model training
RandomForestClassifier(class_weight='balanced')
```

### Model Persistence

```python
import joblib

# Save trained model
joblib.dump(model, 'models/rf_classifier.pkl')

# Load model
model = joblib.load('models/rf_classifier.pkl')
```

## Hyperparameter Tuning

Grid search configuration for Random Forest:

```python
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10]
}
```

## Visualization Examples

The repository generates:
- Feature importance rankings
- Per-electrode mean amplitude by disorder
- Confusion matrices for each classifier
- ROC curves (for binary classification scenarios)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed modifications.

## License

[MIT](LICENSE)

## Citation

If you use this code in your research, please cite:

```bibtex
@software{eeg_classification,
  author = {Your Name},
  title = {EEG-Based Disease Classification},
  year = {2024},
  url = {https://github.com/yourusername/eeg-classification}
}
```

## Contact

GitHub: [@TheRealArithmeticProgression](https://github.com/TheRealArithmeticProgression)

---

**Note**: This is a research/educational project. Models should be validated with appropriate clinical data before any medical application.
⭐ If you found this project helpful, please give it a star!
