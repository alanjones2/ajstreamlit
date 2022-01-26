description = "Home page"

def run():
        
    import streamlit as st

    st.header("""Example Streamlit apps""")
    st.write("""These are a few of the Streamlit apps that I have developed as examples for articles 
    written on Medium.""")
    st.write("""You can select the individual apps from the dropdown menu on the left.
    """)

if __name__ == "__main__":
    run()