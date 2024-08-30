
import streamlit as st

if __name__== "__main__":
    pg = st.navigation([st.Page("sources/Le_Recipinator.py"),
                        st.Page("sources/pages/Ajouter_une_recette.py"),
                        st.Page("sources/pages/Voir_la_base_de_données.py"),
                        st.Page("sources/pages/Modifier_une_recette.py")
                        ])
    pg.run()
