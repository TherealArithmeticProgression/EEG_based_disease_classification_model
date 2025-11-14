# 🧠 EEG-Based Disease Classification

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Multi-class classification of neurological disorders using EEG electrode readings and demographic data.

## Overview

This repository implements machine learning classifiers to predict neurological disorders from 32-channel EEG data combined with participant demographics (age, sex, education, IQ, EQ). The pipeline includes preprocessing, feature engineering, model training, and evaluation.
Electroencephalography (EEG) is a non-invasive neurophysiological technique that measures the electrical activity of the brain by recording voltage fluctuations resulting from ionic current flows within neurons through electrodes placed on the scalp surface. The EEG signal reflects the summation of postsynaptic potentials from large populations of cortical pyramidal neurons firing synchronously, providing temporal resolution in the millisecond range that is essential for capturing the dynamic nature of neural processes. 

EEG electrode data reveals critical information about a patient's neurological status, including cortical function, sleep architecture, level of consciousness, and the presence of pathological activity such as epileptiform discharges, generalized or focal slowing, and asymmetries in brain activity. Clinically, EEG patterns enable the identification and classification of seizure disorders, the assessment of encephalopathies, the evaluation of brain death, the monitoring of sedation depth during anesthesia, and the detection of subtle abnormalities in conditions such as dementia, infections, metabolic disturbances, and structural brain lesions. The spatial distribution, frequency composition, amplitude characteristics, and reactivity of EEG rhythms provide complementary diagnostic information that, when interpreted within the appropriate clinical context, significantly contributes to patient diagnosis, treatment planning, and prognostic evaluation in neurological and psychiatric care.

## Dataset

The dataset contains:
- **Features**: 32 EEG electrode readings, age, sex, education level, IQ, EQ
- **Target**: Disorder/diagnosis classification
- **Format**: CSV with columns for participant demographics and `EEG_Electrode_{1-32}`

## Installation

```bash
git clone https://github.com/TherealArithmeticProgression/EEG_based_disease_classification_model
cd EEG_based_disease_classification_model
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


### Outputs:
 ```
 Confusion matrices
 Classification reports (precision, recall, F1-score)
 Classification visualized
```
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
```
| Model | Accuracy | F1-Score (Weighted) |

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed modifications.

## License

[MIT](LICENSE)

## Citation

If you use this code in your research, please cite:

```bibtex
@software{eeg_classification,
  author = {Akshar Pujara},
  title = {EEG-Based Disease Classification},
  year = {2025},
  url = {https://github.com/TherealArithmeticProgression/EEG_based_disease_classification_model}
}
```

## Contact

GitHub: [@TheRealArithmeticProgression](https://github.com/TheRealArithmeticProgression)
LinkedIn: [@AksharPujara](https://www.linkedin.com/in/akshar2007/)

---

**Note**: This is a research/educational project. Models should be validated with appropriate clinical data before any medical application.
⭐ If you found this project helpful, please give it a star!
