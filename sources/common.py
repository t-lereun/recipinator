from pathlib import Path 
import os
import sqlite3 as sqlite
import pandas as pd

ROOT = Path(__file__).parents[1]

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


