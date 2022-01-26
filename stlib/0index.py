description = "Home page"

def run():
        
    import streamlit as st

    st.header("""Example Streamlit apps""")
    st.write("""These are a few of the Streamlit apps that I have developed as examples for articles 
    written on Medium.""")
    st.write("""You can select the individual apps from the dropdown menu on the left.
    """)
    st.markdown("""And you can find the articles here:""")
    st.markdown("""[An Interactive CO2 Emissions Dashboard with Plotly and Streamlit]
    (https://towardsdatascience.com/an-interactive-co2-emissions-dashboard-with-plotly-and-streamlit-b0bd4ae80cc8)""")
 
    st.markdown("""[Build a Personal Webpage with Streamlit]
    (https://medium.com/geekculture/build-a-promotional-webpage-with-streamlit-4088b87354d2)""")

    st.markdown("""[Rational UI Design with Streamlit]
    (https://towardsdatascience.com/rational-ui-design-with-streamlit-61619f7a6ea4)""")

    st.markdown("""[A Multi-page Interactive Dashboard with Streamlit and Plotly]
    (https://towardsdatascience.com/a-multi-page-interactive-dashboard-with-streamlit-and-plotly-c3182443871a)""")

    st.write("""The links are also in the individual apps.
    """)

if __name__ == "__main__":
    run()