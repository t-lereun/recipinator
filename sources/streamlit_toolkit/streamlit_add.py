import pandas as pd
import sqlite3 as sqlite
from pandas import read_sql_query, read_sql_table
from sources import add_recipe as ar
from sources import init_database, common
import streamlit as st
import os

# st.title('The Recipinator')
DB_DIR = init_database.DB_DIR

def add_db():

    db_name = st.text_input("Nom de la nouvelle base de données (sans extension)",
                  value='recipes')
    
    # Path to db
    db_path = os.path.join(DB_DIR,f"{db_name}.db")

    file_exists = os.path.isfile(db_path)

    db_btn = st.button("Ajouter")
    if db_btn:
        if file_exists:
            msg = "**Il existe déjà une base de donnée portant ce nom !**"
        else: 
            init_database.init_database(db_name)
            msg = "Base de donnée ajoutée !"

        st.markdown(msg)

            
        


def add_recipe(recipe=None, recipe_dict=None):

    if recipe==None:
        recipe_dict = {
            'name':'',
            'cookbook':'',
            'page':'',
            'ingredient_1':'',
            'ingredient_2':'',
            'ingredient_3':'',
            'ingredient_4':'',
            'other_ingredients':'',
            'regime':'',
        }

    
    with st.form('recipe'):

        # These methods called on the form container, so they appear inside the form.
        name = st.text_input('Nom de la recette:', recipe_dict['name'])
        cookbook = st.text_input('Livre:',recipe_dict['cookbook'])
        page = st.text_input('Page',recipe_dict['page'])
        ingredient_1 = st.text_input('Ingredient 1 (indispensable)', 
                                     recipe_dict['ingredient_1'])
        ingredient_2 = st.text_input("Ingredient 2 (difficile de s'en passer)", 
                                     recipe_dict['ingredient_2'])
        ingredient_3 = st.text_input("Ingredient 3 (peut-être qu'on peut imaginer une substitution)",
                                     recipe_dict['ingredient_3'])
        ingredient_4 = st.text_input("Ingredient 4 (ce serait dommage de ne pas en mettre)",
                                     recipe_dict['ingredient_4'])
        other_ingredients = st.text_input("Autres ingrédients (à marmitonner)", 
                                          recipe_dict['other_ingredients'])
        
        submit = st.form_submit_button('Ajouter la recette')


    if submit:
        st.write("Ajout à la base de données...")
        ar.add_recipe(name=name, cookbook=cookbook, page=page, 
                ingredient_1=ingredient_1, ingredient_2=ingredient_2,
                ingredient_3=ingredient_3, ingredient_4=ingredient_4,
                other_ingredients=other_ingredients) 
        st.write("Recette ajoutée !")   


        cnx = sqlite.connect('./recipes/recipes.db')

        df = pd.read_sql_query("SELECT * FROM Recipes", cnx)


        st.dataframe(df)

