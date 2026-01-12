import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Machine Learning System for Residential Property Valuation",
    page_icon="🏠",
    layout="centered"
)

# -------------------------------
# Load Trained Model
# -------------------------------
model = joblib.load("model/property_valuation_model.pkl")

# -------------------------------
# App Title
# -------------------------------
st.title("🏠 House Price Prediction")
st.subheader("Predict house prices using Machine Learning")
st.markdown("---")

# -------------------------------
# Input Section
# -------------------------------
st.header("📋 Property Details")

under_construction = st.selectbox(
    "Under Construction",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

bhk = st.number_input(
    "BHK",
    min_value=1,
    max_value=10,
    step=1,
    value=2
)

square_ft = st.number_input(
    "Square Feet",
    min_value=300,
    max_value=10000,
    value=1000
)

ready_to_move = st.selectbox(
    "Ready to Move",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

resale = st.selectbox(
    "Resale Property",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

longitude = st.number_input(
    "Longitude",
    value=77.590000,
    format="%.6f"
)

latitude = st.number_input(
    "Latitude",
    value=12.970000,
    format="%.6f"
)

posted_by = st.selectbox(
    "Posted By",
    ["Owner", "Dealer"]
)

# -------------------------------
# Encoding
# -------------------------------
posted_by_owner = 1 if posted_by == "Owner" else 0
posted_by_dealer = 1 if posted_by == "Dealer" else 0

FEATURE_COLUMNS = [
    'UNDER_CONSTRUCTION',
    'BHK_NO.',
    'SQUARE_FT',
    'READY_TO_MOVE',
    'RESALE',
    'LONGITUDE',
    'LATITUDE',
    'POSTED_BY_Dealer',
    'POSTED_BY_Owner'
]

# -------------------------------
# Prediction
# -------------------------------
if st.button("💰 Predict Price"):
    input_data = pd.DataFrame([{
        'UNDER_CONSTRUCTION': under_construction,
        'BHK_NO.': bhk,
        'SQUARE_FT': square_ft,
        'READY_TO_MOVE': ready_to_move,
        'RESALE': resale,
        'LONGITUDE': longitude,
        'LATITUDE': latitude,
        'POSTED_BY_Dealer': posted_by_dealer,
        'POSTED_BY_Owner': posted_by_owner
    }])

    input_data = input_data.reindex(columns=FEATURE_COLUMNS, fill_value=0)

    prediction = model.predict(input_data)[0]

    st.success("✅ Prediction Successful")
    st.metric(
        label="Estimated House Price",
        value=f"₹ {prediction:.2f} Lakhs"
    )

