# 💳 Credit Risk Prediction System

A Machine Learning web application built with **Streamlit** that predicts whether a customer is a **Good Credit Risk** or **Bad Credit Risk** using a trained Logistic Regression model.

## 🚀 Features

- Predict customer credit risk
- Logistic Regression model
- One-Hot Encoding preprocessing
- CSV Upload Support
- Download prediction results
- User-friendly Streamlit interface

## 📂 Project Structure

```
Credit_Risk_App/
│── app.py
│── credit_risk_model.pkl
│── feature_names.pkl
│── german_credit_data.csv
│── requirements.txt
│── README.md
```

## 📊 Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest (Performance Comparison)

### Final Model Used

**Logistic Regression**

Performance:

- Accuracy: **79%**
- ROC-AUC: **0.83**

## 📁 Dataset

German Credit Dataset

Features include:

- Account Status
- Credit History
- Credit Amount
- Savings
- Employment
- Age
- Housing
- Purpose
- Job
- Foreign Worker
- and more.

Target Variable:

- Good Credit
- Bad Credit

## ⚙️ Installation

Clone the repository

```bash
git clone <your-repository-link>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

## 🖥️ How to Use

1. Launch the Streamlit application.
2. Upload a CSV file containing customer information.
3. Click upload.
4. View predicted credit risk.
5. Download prediction results as CSV.

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

## 📄 License

This project is developed for educational purposes.
