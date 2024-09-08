import streamlit as st
from sources.streamlit_toolkit import streamlit_add, write_recipe
from sources import add_recipe, common


st.set_page_config(page_title="", page_icon="✏️")

def add_ingredient(ingredient, quantity, units):
    st.write(f'{quantity} {units} de {ingredient}')

def handle_action_two():
    st.write('Action Two Executed')



st.markdown("# Ajouter une recette")
st.sidebar.header("Ajouter d'une recette")

st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)

col = st.columns([0.5, 0.5],gap="medium")

with col[0]:
    # If recipe is in a a book, only add ingredients
    from_cookbook = st.button("J'ai le livre chez moi")

with col[1]:
        oral_recipe = st.button("Je veux écrire la recette")

db_list = common.get_db_list()      

if "from_cookbook" not in st.session_state:
    st.session_state.from_cookbook = False

if "oral_recipe" not in st.session_state:
    st.session_state.oral_recipe = False
    st.session_state.ingredient_list = []

if from_cookbook or st.session_state.from_cookbook:
    db = st.selectbox("Dans quelle base de données?",
                      options=db_list)
    st.session_state.oral_recipe = False
    st.session_state.from_cookbook = True
    streamlit_add.add_recipe(db)

if oral_recipe or st.session_state.oral_recipe:
    db = st.selectbox("Dans quelle base de données?",
                    options=db_list)
    st.session_state.from_cookbook = False
    st.session_state.oral_recipe = True

    title = write_recipe.recipe_title()
    text = write_recipe.recipe_textbox()
    diet = streamlit_add.get_diet()

    recipe_path = write_recipe.save_text(text, title)
    add_recipe.add_from_md(db, recipe_path, diet)


