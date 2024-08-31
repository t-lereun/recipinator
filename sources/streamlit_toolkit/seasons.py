import streamlit as st
import os 
from pathlib import Path 
import yaml
from datetime import datetime

ROOT = Path(__file__).parents[2]

GAZINIERE = {
    'path': os.path.join(ROOT,'filters','gaziniere.yml'),
    'link': 'https://lagaziniere850fcs.wordpress.com/',
    'text': "_La Gazinière_"
}

with open(GAZINIERE['path'], 'r') as file:
    GAZ_DICT = yaml.safe_load(file)
file.close()


def get_month():
    current_time = datetime.now()
    current_month = current_time.strftime("%B")
    return current_month.lower()

def print_list_str(list):
    string = ''
    n = len(list)
    for i in range(n-1):
        string += f"{list[i]}, "
    
    # Add last
    string += f"{list[-1]}.\n\n"

    return string


def gaz_list(key):

    month = get_month()
    gaz_month = GAZ_DICT[month]
    good_list = gaz_month[key]

    # st.markdown(print_list_str(good_list))
    return print_list_str(good_list)


def gaz_show():

    st.write('\n')
    st.markdown('## Avant de faire les courses')
    gaz_markdown = f"[{GAZINIERE['text']}]({GAZINIERE['link']})"
    st.markdown(f"Voici des suggestions d'après {gaz_markdown}.")

    good_list = gaz_list('good')
    best_list = gaz_list('best')

    st.markdown(f"**C'est la saison**: {good_list}")
    st.markdown(f"**C'est la _meilleure_ saison**: {best_list}")