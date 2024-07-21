import streamlit as st
from sources.streamlit_toolkit import streamlit_add



st.set_page_config(page_title="", page_icon="➕")

st.markdown("# Ajouter une recette")
st.sidebar.header("Ajouter d'une recette")

streamlit_add.add_recipe()
