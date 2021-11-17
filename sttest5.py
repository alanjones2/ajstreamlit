import streamlit as st
import pandas as pd
import plotly.express as px

#########################################
######            Model            ######
#########################################

class model():
    def __init__(self):
        self.year = 1952
        self.df = pd.DataFrame(px.data.gapminder())
        self.clist = self.df['country'].unique()
        self.ylist = self.df['year'].unique()
        self.yearStart = int(self.ylist[0])
        self.yearEnd = self.ylist[len(self.ylist)-1]
        self.yearStep = self.ylist[1]-self.ylist[0]
        
    
    def mainChart(self,year):
        return px.scatter(self.df[self.df['year'] == year], 
            x = "lifeExp", y = "gdpPercap", title = str(year),
            color='continent',size='pop')
    def chart(self, country, y, label):
        return px.line(self.df[self.df['country'] == country], 
            x = "year", y = y, title = label)


model = model()

#########################################
######         Page layout         ######
#########################################

st.set_page_config(layout = "wide")

## Header
st.header("Global Statistics")

commentaryCol, chartCol=st.columns((1,2))

with commentaryCol:
    caption="""See how life expectancy changes over time and in relation to GDP.
     Move the slider to change the year to display."""
    st.write(caption)
    
    ## Year Slider
    caption="Select the year for the chart"
    year=st.slider(caption,model.yearStart,2007,1952,5)

with chartCol:
    ## Main Chart

    st.plotly_chart(model.mainChart(year), use_container_width = True)

## Countries Drop down menu

country = st.selectbox("Select a country:", model.clist)

## GDP and Population charts in columns
col1, col2 = st.columns(2)

## GDP column
with col1:
    st.plotly_chart(model.chart(country, "gdpPercap","GDP per Capita"), use_container_width = True)

## Population column
with col2:
    st.plotly_chart(model.chart(country, "pop", "Population"), use_container_width = True)
