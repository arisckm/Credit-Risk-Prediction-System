import streamlit as st
import pandas as pd
import joblib

# Load model and feature names
model = joblib.load("credit_risk_model.pkl")
feature_names = joblib.load("feature_names.pkl")

st.title("💳 Credit Risk Prediction System")

st.write("Upload a customer CSV file to predict credit risk.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.write(data.head())

    # One-Hot Encoding
    data = pd.get_dummies(data)

    # Match training columns
    data = data.reindex(columns=feature_names, fill_value=0)

    # Prediction
    predictions = model.predict(data)

    probabilities = model.predict_proba(data)[:, 1]

    result = pd.DataFrame({
        "Prediction": predictions,
        "Risk Probability": probabilities
    })

    result["Prediction"] = result["Prediction"].map({
        0: "Good Credit",
        1: "Bad Credit"
    })

    st.subheader("Prediction Result")

    st.write(result)

    csv = result.to_csv(index=False).encode('utf-8')

    st.download_button(
        "Download Results",
        csv,
        "credit_predictions.csv",
        "text/csv"
    )