import pandas as pd
import sqlite3 as sqlite
from pandas import read_sql_query, read_sql_table
from sources import add_recipe as ar
import streamlit as st

# st.title('The Recipinator')


def add_recipe():

    with st.form('recipe'):

        # These methods called on the form container, so they appear inside the form.
        name = st.text_input('Nom de la recette:', '')
        cookbook = st.text_input('Livre:','')
        page = st.text_input('Page','')
        ingredient_1 = st.text_input('Ingredient 1 (indispensable)', '')
        ingredient_2 = st.text_input("Ingredient 2 (difficile de s'en passer)", '')
        ingredient_3 = st.text_input("Ingredient 3 (peut-être qu'on peut imaginer une substitution)",'')
        ingredient_4 = st.text_input("Ingredient 4 (ce serait dommage de ne pas en mettre)",'')
        other_ingredients = st.text_input("Autres ingrédients (à marmitonner)", '')
        
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

