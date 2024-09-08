import streamlit as st
from sources.streamlit_toolkit import filters
from sources import common
from sources import process_db
import sqlite3 as sqlite
import pandas as pd
import os 
from pathlib import Path
import webbrowser as wb


st.set_page_config(
page_title="Recherche de recettes",
page_icon="👀",
)

st.markdown("# Voir une base de données")
st.sidebar.header("Voir une base de données")


db_list = common.get_db_list()

filters_dir = os.path.join(Path(__file__).parents[2],'filters')
# # options = os.listdir(db_dir)
# filters = os.listdir(filters_dir)

# print(db_list)

option = st.selectbox(
   "Base de donnée à afficher",
   db_list,
   index=None,
)

# filter = st.selectbox(
#    "Appliquer un filtre (régime alimentaire, etc)",
#    filters,
#    index=None,
# )



ingredients_av = process_db.scrap_ingredients(option)

# ingredient = st.text_input(
#         "Choisir un ingrédient",
#     )



# st.write("You selected:", option)
if not(option==None):


   path_to_db = os.path.join(Path(__file__).parents[2],'recipes',option)

   cnx = sqlite.connect(path_to_db)

   df = pd.read_sql_query("SELECT * FROM Recipes", cnx)

   i = 0
   filter_added = None

   while not(filter_added==None) or i==0:
      filter_added = filters.add_filter_button(i)
      df = filters.apply_filter(df, filter_added, ingredients_av)
      i +=1

   
   keys_to_show = ['name','cookbook','page','ingredient_1',
                   'ingredient_2', 'ingredient_3', 'ingredient_4',
                   'other_ingredients', 'regime']
   
   keys_display = {
      'name':'Recette',
      'cookbook':'Livre/dossier',
      'ingredient_1':'Ingrédient 1',
      'ingredient_2':'Ingrédient 2',
      'ingredient_3':'Ingrédient 3',
      'ingredient_4':'Ingrédient 4',
      'other_ingredients':'Autres ingrédients',
      'regime':'Régime',
      'season score':'Score saison'
   }

   column_configuration = {
    "name": st.column_config.TextColumn(
        "Recette",
    ),
    "cookbook": st.column_config.TextColumn(
        "Livre ou fichier",
    ),
    "page": st.column_config.NumberColumn(
        "Page",
    ),
    "ingredient_1": st.column_config.TextColumn(
        "Ingrédient 1",
    ),
    "ingredient_2": st.column_config.TextColumn(
        "Ingrédient 2",
    ),
    "ingredient_3": st.column_config.TextColumn(
        "Ingrédient 3",
    ),
    "ingredient_4": st.column_config.TextColumn(
        "Ingrédient 4",  
    ),
   "other_ingredients": st.column_config.TextColumn(
        "Autres ingrédients",  
    ),
    "regime": st.column_config.TextColumn(
        "Régime alimentaire",
    ),
    "score season": st.column_config.NumberColumn(
        "Score de saison",
    ),
   }


   selected = st.dataframe(df, hide_index=True,
                           column_config=column_configuration,
                           on_select='rerun',
                           selection_mode="single-row")# column_config=column_config,on_select="rerun")

   selected_row = selected['selection']['rows']


   if len(selected_row)>0:

      recipe_link = df.iloc[selected.selection.rows[0],
                           df.columns.get_loc('cookbook')]

      if os.path.exists(recipe_link):
         text_recipe = common.read_txt(recipe_link)
         st.markdown(text_recipe)