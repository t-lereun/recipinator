import streamlit as st
from sources.streamlit_toolkit import streamlit_add
from sources import process_db
import sqlite3 as sqlite
import pandas as pd
import os 
from pathlib import Path


st.markdown("# Voir une base de données")
st.sidebar.header("Voir une base de données")

# Get the list of databases
db_dir = os.path.join(Path(__file__).parents[2],'recipes')
filters_dir = os.path.join(Path(__file__).parents[2],'filters')
options = os.listdir(db_dir)
filters = os.listdir(filters_dir)

option = st.selectbox(
   "Base de donnée à afficher",
   options,
   index=None,
)

filter = st.selectbox(
   "Appliquer un filtre (régime alimentaire, etc)",
   filters,
   index=None,
)


ingredient = st.text_input(
        "Choisir un ingrédient",
    )


# st.write("You selected:", option)
if not(option==None):

   path_to_db = os.path.join(Path(__file__).parents[2],'recipes',option)

   cnx = sqlite.connect(path_to_db)

   df = pd.read_sql_query("SELECT * FROM Recipes", cnx)

   if not(filter==None):
      df = process_db.filter(df,filter=filter)

   if not(ingredient==None):
      df = process_db.filter_by_ingredient(df,ingredient=ingredient)

   if len(df)==0:
      st.markdown(":red[Aucune recette ne correspond aux critères]")
   else:
      st.dataframe(df)