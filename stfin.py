import pandas as pd
import json
import plotly
import plotly.express as px
import yfinance as yf
import streamlit as st


def getInfo(stock):
    st = yf.Ticker(stock)
    return (st.info)

def getStock(stock,period, interval):
    st = yf.Ticker(stock)
  
    # Create a line graph
    df = st.history(period=(period), interval=interval)
    df=df.reset_index()
    df.columns = ['Date-Time']+list(df.columns[1:])
    max = (df['Open'].max())
    min = (df['Open'].min())
    range = max - min
    margin = range * 0.05
    max = max + margin
    min = min - margin
    fig = px.area(df, x='Date-Time', y="Open",
        hover_data=("Open","Close","Volume"), 
        range_y=(min,max), template="seaborn" )
    return fig


periods = ('1d','5d','1mo','3mo','6mo','1yr','2yr','5yr','ytd','max')
intervals = ('5m','60m','1d','5d','1w','1mo','3mo')
stockNames = ('MSFT','GOOGL','FB','AAPL')

#header
st.header('Stock values over time')

#3 dropdowns stock, period, interval
stockCol, periodCol, intCol = st.columns(3)
with stockCol:
    stockName = st.selectbox('Stock', stockNames)
with periodCol:
    period = st.selectbox('Period', periods)
with intCol:
    interval = st.selectbox('Interval', intervals)

stockInfo = getInfo(stockName)
st.write(stockInfo['shortName'])

fig = getStock(stockName,period,interval)

st.plotly_chart(fig,use_container_width = True)