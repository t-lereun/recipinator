import pandas as pd
import sqlite3 as sqlite
from pandas import read_sql_query, read_sql_table
from sources import add_recipe as ar
from sources import init_database, common, process_db
from sources.streamlit_toolkit import write_recipe
import streamlit as st
import numpy as np

import os

FILTERS = ['Ingrédient', "Saison", "Régime"]

def subfilter_layout():

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

    return col



def filter_number(i):
    res = ''
    if i==0:
        res = '1er'
    else:
        res = f"{i+1}e"
    
    return res

def key_ingredient(i):

    return f"Choisir un {filter_number(i)} ingrédient"

def get_ingredient_key():

    i = 0
    while key_ingredient(i) in st.session_state:
        st.write("\nWARNING\n")
        i+=1

    return i



def add_filter_button(i):

    filter_type = st.selectbox(f"**Ajouter un {filter_number(i)} filtre**",
                               FILTERS,
                               index=None,
                            #    key = f"{np.random.normal()}"
                               )
    
    return filter_type


def apply_filter(df, filter_type, db_ingredients):

    if filter_type=="Ingrédient":

        df = filter_ingredient(df, db_ingredients)

    elif filter_type=="Régime":
        df = filter_diet(df)

    else:
        df = process_db.score_by_season(df)

    return df


def filter_ingredient(df, db_ingredients):

    # print(st.session_state)
    # i = get_ingredient_key()
    # print(key_ingredient(i))

    ingredient = None
    i = 0

    while not(ingredient==None) or i ==0:

        col = subfilter_layout()

        with col[1]:
            ingredient = st.selectbox(
            key_ingredient(i),
            db_ingredients,
            index=None,
            )
        i +=1

    # if not ingredient==None:
        df = process_db.filter_by_ingredient(df, 
                                             ingredient=ingredient)

    return df

def filter_diet(df):

    col = subfilter_layout()

    with col[1]:
        diet = st.selectbox(
            "Sélectionner un régime",
            common.DIETS,
            index=None,
            )

    df = process_db.filter_by_diet(df, diet)

    return df





