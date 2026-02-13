import streamlit as st
import requests

URL = "https://api.exchangerate-api.com/v4/latest/INR"

st.title("Currency Converter")
st.subheader("Convert INR to other currencies")
input_amount = st.number_input("Enter amount in INR", min_value=1, step=1)
target_currency = st.selectbox("Select target currency", options=["USD", "EUR", "GBP", "JPY", "AUD"])

if st.button("Convert"):
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        rates = data["rates"][target_currency]
        converted_amount = input_amount * rates
        st.write(f"{input_amount} INR = {converted_amount:.2f} {target_currency}")
    else:
        st.error("Failed to fetch exchange rates. Please try again later.")