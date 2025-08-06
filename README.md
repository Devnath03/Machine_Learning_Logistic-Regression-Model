# Logistic Regression Model

## Overview
This project demonstrates a complete workflow for building, training, evaluating, and deploying a Logistic Regression model using Python. It is designed for binary classification tasks and includes data preprocessing, model training, evaluation, and model persistence.

## Project Structure
```
logistic_data.csv           # Dataset used for training/testing
Logistic_Regression.ipynb   # Jupyter notebook for interactive exploration
main.py                     # Main script for model training and evaluation
model.pickle                # Serialized trained model
```

## Features
- Data loading and preprocessing
- Model training using Logistic Regression
- Model evaluation (accuracy, confusion matrix, etc.)
- Model serialization (pickle)
- Jupyter notebook for step-by-step analysis

## Getting Started

### Prerequisites
- Python 3.7+
- pip
- Recommended: virtual environment (venv or conda)

### Installation
1. Clone the repository:
   ```powershell
   git clone https://github.com/Devnath03/Machine_Learning_Logistic-Regression-Model.git
   cd Machine_Learning_Logistic-Regression-Model
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install manually:
   ```powershell
   pip install numpy pandas scikit-learn matplotlib
   ```

### Usage
#### 1. Run the Jupyter Notebook
   ```powershell
   jupyter notebook Logistic_Regression.ipynb
   ```
   - Explore data, train model, and visualize results interactively.

#### 2. Run the Main Script
   ```powershell
   python main.py
   ```
   - Loads data, trains model, evaluates, and saves the model as `model.pickle`.

#### 3. Use the Trained Model
   - Load `model.pickle` in your own scripts to make predictions on new data.

## Data
- `logistic_data.csv` should be a CSV file with features and a binary target column.
- Example columns: `feature1`, `feature2`, ..., `target`

## Model Details
- **Algorithm:** Logistic Regression (from scikit-learn)
- **Evaluation Metrics:** Accuracy, Confusion Matrix, Precision, Recall, F1-score
- **Serialization:** Pickle

## Customization
- Modify `main.py` to change preprocessing, model parameters, or evaluation metrics.
- Extend the notebook for additional analysis or visualization.

## Example Code Snippet
```python
import pickle
from sklearn.linear_model import LogisticRegression
# ...existing code...
model = LogisticRegression()
model.fit(X_train, y_train)
with open('model.pickle', 'wb') as f:
    pickle.dump(model, f)
```

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Author
- [Devnath03](https://github.com/Devnath03)

## References
- [Scikit-learn Documentation](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
- [Logistic Regression Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression)
