import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

data = fetch_california_housing(as_frame=True)
df = data.frame

scaler = StandardScaler()
X = df.drop('MedHouseVal', axis=1)  
X_scaled = scaler.fit_transform(X)

# Training the model
rf_model = RandomForestRegressor()
rf_model.fit(X_scaled, df['MedHouseVal'])  
st.title("California Housing Price Prediction")
st.image("house.jpeg", caption="House Price Prediction",width=700)

feature_names = X.columns.tolist()
input_values = []  

for feature in feature_names:
    input_values.append(st.number_input(feature, value=0.0)) # Default value set to 0.0

# Creating a dataframe for prediction
input_data = pd.DataFrame([input_values], columns=X.columns)


# Scale input data
input_scaled = scaler.transform(input_data)

# Predicting the output
if st.button(":green[Predict Price]"):
    predicted_price = rf_model.predict(input_scaled)
    st.success(f"The predicted house price is: ${predicted_price[0] * 100000:.2f}")
