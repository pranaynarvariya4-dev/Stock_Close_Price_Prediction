import streamlit as st 
import joblib


model = joblib.load("stock_model.pkl")
st.title("Stock  Price Close Prediction")
open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")      
low_price = st.number_input("Low Price")
total_trade_quantity = st.number_input("total_trade_quantity")
turnover_in_lacks = st.number_input("turnover_in_lacks")
if st.button("Predict"):
    input_data = [[open_price, high_price, low_price, total_trade_quantity, turnover_in_lacks]]
    predicted_price = model.predict(input_data)[0]
    st.write(f"Predicted Close Price: ${predicted_price:.2f}")   


st.markdown("""
<style>body {
    background-color: #f0f0f0;)
    font-family: 'Arial', sans-serif;
}
            .stButton>button{width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            border: none;}
            .stButton>button:hover{background-color: #45a049;
            .stButton>button:active{background-color: #3e8e41;
            color: white;} 
            h1{
            color: #333;
            text-align: center; 
            font-family: 'Arial', sans-serif;}   
            </style>
""", unsafe_allow_html=True)