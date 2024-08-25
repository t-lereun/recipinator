import sqlite3
from sources.init_database import keys
import os
from pathlib import Path

DEFAULT_DB = os.path.join(Path(__file__).parents[1],'recipes','recipes.db')
print(str(DEFAULT_DB))
# "./recipes/recipes.db"



def add_recipe(database= DEFAULT_DB, 
               name=None, cookbook=None, page=None, 
               ingredient_1=None, ingredient_2=None,
               ingredient_3=None, ingredient_4=None,
               other_ingredients=None, regime=None):
    
    conn = sqlite3.connect(database)
    c = conn.cursor()

    recipe_dict = {
        'name':name,
        'cookbook':cookbook,
        'page':page,
        'ingredient_1':ingredient_1,
        'ingredient_2':ingredient_2,
        'ingredient_3':ingredient_3,
        'ingredient_4':ingredient_4,
        'other_ingredients':other_ingredients,
        'regime':regime,
    }


    str_k_list = ''
    val_str  = ''
    for k in keys:
        str_k_list += f' {k}, '
        val_str += f"'{recipe_dict[k]}', "
        

    
    # sql = 'INSERT INTO Recipes(name, servings, source) VALUES("Pasta with bacon and tomato sauce", 3, "Arthur Ngondo")'
    sql = f'INSERT INTO Recipes({str_k_list[:-2]}) VALUES({val_str[:-2]})'

    print(sql)

    c.execute(sql)


    conn.commit()

def get_all_recipes(database=DEFAULT_DB):

    conn = sqlite3.connect('./recipes/recipes.db')#sqlite3.connect(database)
    c = conn.cursor()
    # conn.row_factory = lambda cursor, row: row[0]

    # Fetch all lines
    rows = c.execute(f"SELECT name from Recipes").fetchall()

    rows = [r[0] for r in rows]

    return rows

def find_from_name(database=DEFAULT_DB, name=None):

    #conn = sqlite3.connect('./recipes/recipes.db')
    #conn = sqlite3.connect("/home/tlereun/recipinator/recipes/recipes.db")
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute(f"SELECT id from Recipes WHERE name='{name}'")
    ids = c.fetchall()

    return ids

def delete_recipe(database=DEFAULT_DB, name=None,):

    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute(f"DELETE from Recipes WHERE name='{name}'")
    conn.commit()

# row factory (should be moved elsewhere
# 
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_recipe_dict(database=DEFAULT_DB, name=None):

    conn = sqlite3.connect(database)
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Find which line
    c.execute(f"SELECT * from Recipes WHERE name='{name}'")
    recipe_dict = c.fetchone()

    return recipe_dict


def modify_recipe(database= DEFAULT_DB, name=None, keys_modify = [], values=[]):

    

    conn = sqlite3.connect(database)
    c = conn.cursor()


    # Find which line
    c.execute(f"SELECT * from Recipes WHERE name='{name}'")
    rows = c.fetchone()
    print(rows)



    # AJOUTER GARDE-FOU RECETTE AVEC PLUSIEURS NOMS

    for i, k in enumerate(keys_modify):

        if type(values[i]) == str:
            update_statement = f"UPDATE Recipes SET {k}='{values[i]}' WHERE name ='{name}'"
        else: 
            update_statement = f"UPDATE Recipes SET {k}={values[i]} WHERE name ='{name}'"

        c.execute(update_statement)

    c.execute(f"SELECT * from Recipes WHERE name='{name}'")
    rows = c.fetchone()
    print(rows)

    conn.commit()

