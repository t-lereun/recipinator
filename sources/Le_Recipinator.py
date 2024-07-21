import streamlit as st


st.set_page_config(
page_title="Le Recipinator: accueil",
page_icon="mioum",
)

st.markdown(
    """
    #  Le Recipinator

    _Le Recipinator_ est un programme pour collecter et trier les recettes
    en fonction des ingrédients, des saisons, et du régime alimentaire... 
    Du moins c'est ce qu'il aspire à devenir à mesure que le projet se 
    développera. 
"""
)


# def add_recipe():
#     import streamlit as st

#     st.markdown(f"# Ajout d'une recette")


#     streamlit_add.add_recipe()

# page_names_to_funcs = {
#     "—": intro,
#     "Ajout d'une recette": add_recipe,
# }

# if __name__=="__main__":

#     demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
#     page_names_to_funcs[demo_name]()