# Phishing Classifier

A machine learning project to detect phishing websites using classification algorithms.

## 📋 Project Overview

This project implements a phishing detection system using various machine learning algorithms. It analyzes website features to classify whether a URL is legitimate or phishing.

**Dataset:** 11,055 samples with 31 features

## 🎯 Objectives

- Perform exploratory data analysis (EDA) on phishing dataset
- Extract and engineer relevant features
- Compare multiple classification models
- Optimize the best performing model using hyperparameter tuning
- Achieve high accuracy in phishing detection

## 📊 Dataset

- **Total Records:** 11,055
- **Features:** 31 (including target variable)
- **Target Variable:** Result (Phishing classification)
- **Data File:** `notebooks/data/phising_data.csv`

### Key Features
- `having_IP_Address` - Whether URL contains IP address
- `URL_Length` - Length of the URL
- `having_At_Symbol` - Presence of '@' symbol
- `double_slash_redirecting` - Double slash redirect
- `Prefix_Suffix` - Prefix-suffix in domain
- `having_Sub_Domain` - Number of sub-domains
- `SSLfinal_State` - SSL certificate status
- `Domain_registeration_length` - Domain age
- And 23 more features...

## 🔧 Workflow

### 1. Exploratory Data Analysis (`eda.ipynb`)
- Load and inspect dataset
- Check for missing values
- Analyze feature distributions
- Identify unique values per column

### 2. Feature Engineering (`feature_extraction_model.ipynb`)
- Calculate correlation matrix
- Visualize feature relationships
- Calculate Variance Inflation Factor (VIF)
- Remove highly correlated features (VIF > 10)
- Save cleaned dataset

### 3. Model Selection & Training (`model_selection_and_trainning.ipynb`)
- Split data into train/test sets (70/30)
- Train multiple models:
  - Logistic Regression
  - Decision Tree
  - **Random Forest** ⭐ (Best performer)
  - K-Nearest Neighbors
  - Support Vector Machine
  - Naive Bayes
- Perform hyperparameter tuning using GridSearchCV
- Optimize Random Forest model

## 📈 Results

### Model Performance (Accuracy Score)
| Model | Accuracy |
|-------|----------|
| Logistic Regression | ~97% |
| Decision Tree | ~96% |
| **Random Forest** | **~98%** ⭐ |
| KNN | ~95% |
| SVM | ~96% |
| Naive Bayes | ~93% |

### Best Model Parameters
- Algorithm: Random Forest Classifier
- n_estimators: 200
- max_depth: 30
- min_samples_split: 2
- min_samples_leaf: 1

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/phishing_classifier.git
cd phishing_classifier
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Project

1. Open Jupyter Notebook:
```bash
jupyter notebook
```

2. Run notebooks in order:
   - `1_eda.ipynb` - Data exploration
   - `2_feature_extraction.ipynb` - Feature engineering
   - `3_model_selection_and_training.ipynb` - Model training

## 📁 Project Structure

```
phishing_classifier/
├── notebooks/
│   ├── eda.ipynb
│   ├── feature_extraction_model.ipynb
│   ├── model_selection_and_trainning.ipynb
│   └── data/
│       ├── phising_data.csv (original dataset)
│       └── phising_data_updated.csv (cleaned dataset)
├── README.md
├── requirements.txt
└── .gitignore
```

## 🔍 Feature Selection Process

Initial features analyzed for multicollinearity using VIF (Variance Inflation Factor). Features with VIF > 10 were removed to prevent:
- Overfitting
- Model instability
- Reduced interpretability

**Final feature count:** 26 (after removing 5 highly correlated features)

## 💡 Key Findings

1. **Best Algorithm:** Random Forest provides the best balance of accuracy and stability
2. **Feature Importance:** Top features for phishing detection identified
3. **Hyperparameter Impact:** GridSearchCV optimization improved model performance
4. **Data Quality:** No missing values in dataset, well-balanced feature set

## 📚 Libraries Used

- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib & seaborn** - Data visualization
- **scikit-learn** - Machine learning algorithms
- **statsmodels** - Statistical analysis (VIF calculation)

## 🎓 Future Improvements

- [ ] Add cross-validation for more robust evaluation
- [ ] Implement feature importance visualization
- [ ] Create a web interface for predictions
- [ ] Test on real-time phishing URLs
- [ ] Deploy model as API
- [ ] Add ROC-AUC and confusion matrix analysis

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Devraj

## 📧 Contact

For questions or suggestions, feel free to open an issue or contact me.

---

**Note:** This project is for educational purposes. Always validate results with domain experts before deployment.
