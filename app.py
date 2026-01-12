import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/property_valuation_model.pkl")

# Define feature columns (MUST match training data)
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

print("🏠 House Price Prediction App")
print("-" * 35)

# Take user inputs
under_construction = int(input("Under Construction? (0 = No, 1 = Yes): "))
bhk = int(input("Number of BHK: "))
square_ft = float(input("Square Feet: "))
ready_to_move = int(input("Ready to Move? (0 = No, 1 = Yes): "))
resale = int(input("Resale? (0 = No, 1 = Yes): "))
longitude = float(input("Longitude: "))
latitude = float(input("Latitude: "))

posted_by = input("Posted By (Owner / Dealer): ").strip().lower()

# Encode posted_by
posted_by_dealer = 1 if posted_by == "dealer" else 0
posted_by_owner = 1 if posted_by == "owner" else 0

# Create input DataFrame
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

# Ensure column order matches training
input_data = input_data.reindex(columns=FEATURE_COLUMNS, fill_value=0)

# Predict
predicted_price = model.predict(input_data)[0]

print("\n💰 Estimated House Price:")
print(f"👉 {predicted_price:.2f} Lakhs")
