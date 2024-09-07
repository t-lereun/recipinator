from pathlib import Path 
import os
import sqlite3 as sqlite
import pandas as pd
from glob import glob
import numpy as np

ROOT = Path(__file__).parents[1]

DIETS = ['Végé', "Vegan", "Omni (grr)"]

def db_to_df(db_name):

    name, ext = os.path.splitext(db_name)
    print(name, len(ext))

    if len(ext)==0: 
        print('no ext')
        db_name += '.db'
    path_to_db = os.path.join(ROOT,'recipes',db_name)
    print(path_to_db)

    cnx = sqlite.connect(path_to_db)
    df = pd.read_sql_query("SELECT * FROM Recipes", cnx)

    return df


def read_txt(path):

    
    with open(path, 'r') as file:
        file_content = file.read()
    file.close()
    
    return file_content

def get_db_list():

    
    path_to_db_dir = os.path.join(ROOT,'recipes')
    print(path_to_db_dir)
    list_db = glob(path_to_db_dir+'/*.db')
    print(list_db)


    name_lists = np.array([os.path.split(l)[-1] for l in list_db])

    return name_lists



