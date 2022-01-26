import pandas as pd
import json
import plotly
import plotly.express as px
import yfinance as yf
import streamlit as st

description = "Stock Tracker (beta)"

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

def run():
    periods = ('1d','5d','1mo','3mo','6mo','1yr','2yr','5yr','ytd','max')
    intervals = ('1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')
    stockNames = ('MSFT','GOOGL','FB','AAPL')

    #header
    st.header('Experimental Stock Tracker in Streamlit with data from yfinance')
    st.markdown('''Select a stock from the drop down menu, then a period over which
    you want to see the price changes. Finally, select an interval; this will adjust the 
    number of data points within the period.
    You should bear in mind that not all intervals work with all periods, for example,
    you can't use a one minute interval over a long period; if you get a blank chart 
    try a different interval or period.''')

    st.warning('__This app is incomplete and pretty flaky. Do NOT use it for anything serious - just look at the pretty graphs__')

    #3 dropdowns stock, period, interval
    stockCol, periodCol, intCol = st.columns(3)
    with stockCol:
        stockName = st.selectbox('Stock', stockNames)
    with periodCol:
        period = st.selectbox('Period', periods)
    with intCol:
        interval = st.selectbox('Interval', intervals)

    infoCol, chartCol = st.columns((1,3))
    stockInfo = getInfo(stockName)
    with infoCol:
        st.markdown(f"### {stockInfo['shortName']}")
        st.markdown(f"__Day low__: {stockInfo['dayLow']}")
        st.markdown(f"__Day high__: {stockInfo['dayHigh']}")

    with chartCol:
        fig = getStock(stockName,period,interval)
        st.plotly_chart(fig,use_container_width = True)

    
    st.markdown('''
        __This data is to the best of our knowledge accurate but definitely not 
        guaranteed.__ Data supplied by _yfinance._
    ''')

if __name__ == "__main__":
    run()