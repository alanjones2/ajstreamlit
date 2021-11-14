import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")

df = pd.DataFrame(px.data.gapminder())

st.dataframe(df)



st.header("Global Statistics")


year=st.slider("Year",1952,2007,1952,5)
fig = px.scatter(df[df['year'] == year], 
    x = "lifeExp", y = "gdpPercap", title = str(year),color='continent',size='pop')
st.plotly_chart(fig,use_container_width = True)




## Countries
clist = df['country'].unique()

country = st.selectbox("Select a country:",clist)
col1, col2 = st.columns(2)
with col1:
    fig = px.line(df[df['country'] == country], x = "year", y = "gdpPercap",title = "GDP per Capita")
    st.plotly_chart(fig,use_container_width = True)

with col2:
    fig = px.line(df[df['country'] == country], 
		    x = "year", y = "pop",title = "Population Growth")
    st.plotly_chart(fig,use_container_width = True)
st.dataframe(df[df['year'] == year])



