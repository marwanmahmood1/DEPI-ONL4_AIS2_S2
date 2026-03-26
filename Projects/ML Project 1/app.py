import streamlit as st
import pickle
import numpy as np

# Load the saved model
# Make sure 'boston_housing_model.pkl' is in the same folder as this script
try:
    with open('boston_housing_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'boston_housing_model.pkl' is in the directory.")

# Build the Web App UI
st.title("🏡 Boston Housing Price Predictor")
st.write("Enter the features of the neighborhood to get a predicted home price.")

# Create input fields for the 3 features used in your notebook
st.subheader("Property Features")
rm = st.number_input("Average number of rooms (RM)", min_value=1.0, max_value=20.0, value=5.0, step=0.5)
lstat = st.number_input("Neighborhood poverty level % (LSTAT)", min_value=0.0, max_value=100.0, value=17.0, step=1.0)
ptratio = st.number_input("Student-to-teacher ratio (PTRATIO)", min_value=1.0, max_value=50.0, value=15.0, step=0.5)

# Create a button to trigger the prediction
if st.button("Predict Price"):
    # Format the inputs into a 2D array, just like 'client_data' in your notebook
    client_data = [[rm, lstat, ptratio]]
    
    # Generate the prediction
    prediction = model.predict(client_data)[0]
    
    # Display the result
    st.success(f"### Predicted Selling Price: ${prediction:,.2f}")