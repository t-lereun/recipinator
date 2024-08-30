import streamlit as st
from pathlib import Path
import os

RECIPES_PATH = os.path.join(Path(__file__).parents[2],
                    "recipes","personal_recipes")

os.makedirs(RECIPES_PATH,exist_ok=True)

# Default recipe extension
EXT = 'md'


# Default text
ingredient_default = "# Ingrédients\n"
# ingredient_default += "\n" + 30*"=" +"\n"
ingredient_default += "\n- 200 g de sel\n"

instructions_default = "\n# Instructions\n"
# instructions_default += "\n" + 30*"=" +"\n"
instructions_default += "\n1. Verser dans la terrine, verser dans la terrine"

recipe_default = ingredient_default + instructions_default

# Height of the text area
HEIGHT = 500 # pix


def recipe_textbox():

    label = "**Ma recette**"
    text = st.text_area(label, value=recipe_default, 
                height=HEIGHT,
                key='recipe_area',) 
    
    return text

def write_to_file(path, text):

    with open(path,'w') as f:
        f.write(text)
    f.close()
        


def save_text(text):

    with st.form(key='recipe_name'):
        name_txt = "Comment s'appelle la recette ?"
        recipe_name = st.text_input(name_txt, 
                                    key='name_input')
        recipe_name.replace(' ','_')
        text_button = "C'est _moi_ qui l'ai fait"
        save_recipe = st.form_submit_button(text_button)

    if save_recipe:
        recipe_path = os.path.join(RECIPES_PATH,
                                   f"{recipe_name}.{EXT}")

        if os.path.isfile(recipe_path):
            error_msg = "**Il existe déjà une recette portant ce nom !**"
            st.markdown(error_msg)
            force_btn = st.button("**Engregistrer quand même !**")
            
            if force_btn:
                write_to_file(recipe_path, text)

        else: 
            write_to_file(recipe_path, text)
            

        

