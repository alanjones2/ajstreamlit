import streamlit as st
import pandas as pd
import plotly.express as px

#st.set_page_config(layout = "wide")

df = pd.DataFrame(px.data.gapminder())

country_list = df['country'].unique()

# Page layout starts here

st.header("Global Statistics")
st.write("Here are some graphs derived from the Gapminder data that is included in the Plotly package")

## Now the columns

## Countries

country = st.selectbox("Select a country:",country_list)
df_country = df[df['country'] == country]

col1, col2 = st.columns(2)
with col1:
    fig = px.line(df_country, x = "year", y = "gdpPercap",
        title = "GDP per Capita")
    st.plotly_chart(fig,use_container_width = True)

with col2:
    fig = px.line(df_country, x = "year", y = "pop",
        title = "Population Growth")
    st.plotly_chart(fig,use_container_width = True)





