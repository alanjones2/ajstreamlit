############################################ 
# A simple model/view template for Streamlit 
############################################
import streamlit as st

description = "template"

################ Model ################
class Model:
   caption = "This is some text"

################ View  ################
def view(model):
    st.write(model.caption)

################ Start  ################
view(Model())
