#  import library
import streamlit as st
import requests


#  Function to fetch live exchange rates
def get_exchange_rate(from_currency,to_currency):

    #  there is no requirement of api it gives public api and gives live results related to currencies
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    # send requests to api so that we recieve data
    response= requests.get(url)
   

# if api don't give correct response return none
    if response.status_code != 200:
        return None

# data stores the entire result in json file
    data = response.json()
    
    # receive rates where conversion of all currencies are mentioned
    rates = data.get("rates",{})
    
    # it return the target rate of specific currency
    # if there is key then return its value otherwise return None
    return rates.get(to_currency,None)
#  Streamlit UI
st.set_page_config(page_title="Currency Converter", layout="centered")

st.title(" Real-Time Currency Converter")
st.write("Convert currency values instantly using live exchange rates.")

#  User Inputs 
# min_value = 0.0 means negtives are not allowed
# format = it shows upto 2 digits
amount = st.number_input("Enter amount:", min_value=0.0, format="%.2f")
from_currency = st.selectbox("From Currency:", ["USD", "INR", "EUR", "GBP", "JPY", "AUD", "CAD"])
to_currency = st.selectbox("To Currency:", ["USD", "INR", "EUR", "GBP", "JPY", "AUD", "CAD"])

# Convert Button 
if st.button("Convert "):
    # warning appear if both input currency and output are same
    if from_currency == to_currency:
        st.warning("Both currencies are same. Please choose different ones.")
    else:
        # otherwise fetch the exchange rate from api
        rate = get_exchange_rate(from_currency, to_currency)
# if api return the valid rate 
        if rate:
            # conversion formula 
            converted_amount = amount * rate
            st.success(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
            st.caption(f"Exchange Rate: 1 {from_currency} = {rate:.2f} {to_currency}")
        else:
            st.error("Unable to fetch exchange rate. Please try again later.")

#  Footer 
st.markdown("---")
