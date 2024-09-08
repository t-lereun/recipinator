import streamlit as st
from pathlib import Path
from sources import common
import os

RECIPES_PATH = os.path.join(Path(__file__).parents[2],
                    "recipes","personal_recipes")

os.makedirs(RECIPES_PATH,exist_ok=True)

# Default recipe extension
EXT = 'md'


# Default text
ingredient_default = "## Ingrédients\n"
# ingredient_default += "\n" + 30*"=" +"\n"
ingredient_default += "\n- 200 g de sel\n"

instructions_default = "\n## Instructions\n"
# instructions_default += "\n" + 30*"=" +"\n"
instructions_default += "\n1. Verser dans la terrine, verser dans la terrine"

recipe_default = ingredient_default + instructions_default

# Height of the text area
HEIGHT = 500 # pix

def recipe_title():
    title = st.text_input("**Comment s'appelle la recette ?**", 
                          "")
    
    return title

def recipe_textbox(default=recipe_default):

    label = "**Ingrédients et instructions** (_en markdown_)"
    text = st.text_area(label, value=default, 
                height=HEIGHT,
                key='recipe_area',) 
    
    return text

def write_to_file(path, text, title):

    # Add title to text
    text = f"# {title}\n\n" + text 

    print("printing" ,text)

    with open(path,'w') as f:
        f.write(text)
    f.close()


# Function to update the value in session state
def clicked(button):
    st.session_state.clicked[button] = True      


def save_text(text, title):

    # Initialize the key in session state
    if 'clicked' not in st.session_state:
        st.session_state.clicked = {1:False,2:False}


    recipe_name= title.replace(' ','_')
    text_button = "C'est _**moi**_ qui l'ai fait"
    st.button(text_button, on_click=clicked, args=[1])


    if st.session_state.clicked[1]:
        recipe_path = os.path.join(RECIPES_PATH,
                                   f"{recipe_name}.{EXT}")

        if os.path.isfile(recipe_path):
            error_msg = "**Il existe déjà une recette portant ce nom !**"
            st.markdown(error_msg)
            force_btn = st.button("**Engregistrer quand même !**")
            print("FORCE ?",force_btn)

            if force_btn:
                print("FORCE")
                write_to_file(recipe_path, text, title)
                print(" FORCE" , text)
                # text = f"# {title}\n\n" + text 

        else: 
            write_to_file(recipe_path, text, title)

        # text = f"# {title}\n\n" + text 
        st.markdown(text)

        return recipe_path
                

        

