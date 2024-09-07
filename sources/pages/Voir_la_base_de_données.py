import streamlit as st
from sources.streamlit_toolkit import filters
from sources import common
from sources import process_db
import sqlite3 as sqlite
import pandas as pd
import os 
from pathlib import Path


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

#    ingredient = st.selectbox(
#       "Choisir un ingrédient",
#       ingredients_av,
#       index=None,
#    )


   path_to_db = os.path.join(Path(__file__).parents[2],'recipes',option)
   st.write(path_to_db)

   cnx = sqlite.connect(path_to_db)

   df = pd.read_sql_query("SELECT * FROM Recipes", cnx)

   i = 0
   filter_added = None

   while not(filter_added==None) or i==0:
      filter_added = filters.add_filter_button(i)
      df = filters.apply_filter(df, filter_added, ingredients_av)
      i +=1

   st.dataframe(df)



   # # if not(filter==None):
   # #    df = process_db.filter(df,filter=None)
   # #    process_db.scrap_ingredients(option)

   # if not(ingredient==None):
   #    df = process_db.filter_by_ingredient(df,ingredient=ingredient)

   # if len(df)==0:
   #    st.markdown(":red[Aucune recette ne correspond aux critères]")
   # else:
   #    st.dataframe(df)