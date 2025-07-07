import yfinance as yf # Importing yfinance to fetch stock data
import streamlit as st # Importing Streamlit for the web app
import pandas as pd # Importing pandas for data manipulation


st.write("""
# Stock Price App

Shown are the stock closing price and volume of Google!

""")

# You can change this to any stock ticker symbol you want
# For example, 'AAPL' for Apple, 'MSFT' for Microsoft, etc.
tickerSymbol = 'GOOGL'  
# Get the ticker data
tickerData = yf.Ticker(tickerSymbol) 
# Get the historical data
tickerDf = tickerData.history(period='5y')

st.write(f"## {tickerSymbol} Closing Price")
st.line_chart(tickerDf.Close)
st.write(f"## {tickerSymbol} Volume Price")
st.line_chart(tickerDf.Volume)