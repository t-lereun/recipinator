import streamlit as st
from sources.streamlit_toolkit import streamlit_add, write_recipe
from sources import common
from sources import add_recipe
import os 
from pathlib import Path

st.set_page_config(page_icon="📝")
st.markdown("# Modifier une recette")
st.sidebar.header("Modifier une recette")



# Get the list of databases
db_dir = os.path.join(Path(__file__).parents[2],'recipes')
filters_dir = os.path.join(Path(__file__).parents[2],'filters')
options = common.get_db_list()
filters = os.listdir(filters_dir)

database = st.selectbox(
   "Base de données des recettes",
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
    

    if recipe is not None:

        recipe_dict = add_recipe.get_recipe_dict(database=path_to_db, 
                                                 name=recipe)
        recipe_source = recipe_dict['cookbook']

        if os.path.exists(recipe_source):
            # Load text
            recipe_text = common.read_txt(recipe_source)
            # strip the title
            sections = recipe_text.split("\n## ",maxsplit=1)
            text = sections[1]
            text = "## " +text

            text = write_recipe.recipe_textbox(default=text)
            diet = recipe_dict['regime']
            diet_index = common.DIETS.index(diet)
            diet = streamlit_add.get_diet(default=diet_index)
            recipe_source = write_recipe.save_text(text, recipe)
            add_recipe.add_from_md(recipe_source, diet)

        else:
            streamlit_add.add_recipe(recipe, recipe_dict)




        
    # Check if the path to the recipe is valid



# if not(recipe==None):

#     print("in st", recipe_dict)

#     streamlit_add.add_recipe(recipe, recipe_dict)





    

    










