import streamlit as st

st.set_page_config(layout = "wide")

page = st.sidebar.selectbox('Select app',['Global stats','Rational UI Design'])#,'Finance']) 
if page == 'Global stats':
	from stlib import sttest4
	sttest4.run()
elif page == 'Rational UI Design':
	from stlib import rat1
	rat1.run()
elif page == 'Finance':
	from stlib import stfin
	stfin.run()