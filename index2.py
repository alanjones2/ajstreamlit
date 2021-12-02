import streamlit as st

st.set_page_config(layout = "wide")

import pkgutil
import importlib

import stlib
package = stlib

names = []
modules = []
descriptions = [] 

def format_func(name):
    return descriptions[names.index(name)]

for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    print ("Found submodule %s (is a package: %s)" % (modname, ispkg))
    if modname != "_init_":
        m = importlib.import_module('.'+modname,'stlib')
        names.append(modname)
        modules.append(m)
        descriptions.append(m.description)

page = st.sidebar.selectbox('Select app',names, format_func=format_func) 

modules[names.index(page)].run()
