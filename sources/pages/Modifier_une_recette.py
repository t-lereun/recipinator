import streamlit as st
from sources.streamlit_toolkit import streamlit_add
from sources import process_db
from sources import add_recipe
import sqlite3 as sqlite
import pandas as pd
import os 
from pathlib import Path


st.markdown("# Modifier une recette")
st.sidebar.header("Modifier une recette")



# Get the list of databases
db_dir = os.path.join(Path(__file__).parents[2],'recipes')
filters_dir = os.path.join(Path(__file__).parents[2],'filters')
options = os.listdir(db_dir)
filters = os.listdir(filters_dir)

database = st.selectbox(
   "Base de donnée à afficher",
   options,
   index=None,
)


recipe = None
recipe_dict = None

if not(database==None):

    path_to_db = os.path.join(Path(__file__).parents[2],'recipes',database)

    # Get the list of recipe names
    recipe_names = add_recipe.get_all_recipes(path_to_db)

    recipe = st.selectbox(
        "Recette à modifier",
        recipe_names,
        index=None,
        )
    
    recipe_dict = add_recipe.get_recipe_dict(database=path_to_db, name=recipe)
    

if not(recipe==None):

    print("in st", recipe_dict)

    streamlit_add.add_recipe(recipe, recipe_dict)





    

    










