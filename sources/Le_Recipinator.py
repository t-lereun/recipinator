import streamlit as st
from sources.streamlit_toolkit import seasons
from sources import common
import os
from sources import init_database
from sources.streamlit_toolkit import streamlit_add


st.set_page_config(
page_title="Accueil",
page_icon="🥕",
)

# Get the text
introduction_path = os.path.join(common.ROOT,'msg','introduction.md')
introduction_txt = common.read_txt(introduction_path)

st.markdown(introduction_txt)

seasons.gaz_show()

# Check if db exist
db_exists, db_list = init_database.check_db()

st.markdown("## Gestion des bases de données")

if not(db_exists):
    st.markdown("**Il n'existe aucune base de données de recettes**  ")

else: 
    st.markdown("Voici les bases de données existantes")

    for db in db_list:
        path, filename = os.path.split(db)
        st.markdown(f"- {filename}")

st.markdown("**En ajouter une nouvelle ?**")
streamlit_add.add_db()