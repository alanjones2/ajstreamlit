import streamlit as st
import pandas as pd
import plotly.express as px

description = """Rational UI"""


################ Model ################
class Model:
    def __init__(self):
        self.df = pd.DataFrame(px.data.gapminder())
        self.clist = self.df['country'].unique() 
        self.ylist = [int(i) for i in self.df['year'].unique()] # convert to int
        self.yearStart = self.ylist[0]
        self.yearEnd = self.ylist[-1]
        self.yearStep = self.ylist[1]-self.ylist[0]
        
    def chart(self,year):
        return px.scatter(self.df[self.df['year'] == year], 
            x = 'lifeExp', y = 'gdpPercap', title = f'Year: {year}',
            color='continent',size='pop')
        
    header = 'Global Statistics from Gapminder'
    description ='''
        See how life expectancy changes over time and in relation to GDP.
        Move the slider to change the year to display.
    '''
    sliderCaption="Select the year for the chart"

################ View  ################
def view(model):
    

    ## Header
    st.header(model.header)
    st.markdown("""_See related article here:  [Rational UI Design with Streamlit]
    (https://towardsdatascience.com/rational-ui-design-with-streamlit-61619f7a6ea4)_""")

    commentaryCol, spaceCol, chartCol=st.columns((2,1,6))

    # Description
    with commentaryCol:
        with st.container():
            st.write('')
            st.write('')
            st.markdown(model.description)
        
        ## Year Slider
        st.write('')
        st.write('')
        year=st.slider(model.sliderCaption,
            model.yearStart,model.yearEnd,model.yearStart,model.yearStep)

    #Chart
    with chartCol:
        st.plotly_chart(model.chart(year), use_container_width = True)

################ Start  ################
def run():
    view(Model())

if __name__ == "__main__":
    run()