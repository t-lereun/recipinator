import sqlite3
from sources.init_database import keys
import os
from pathlib import Path
import re

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
        'regime':regime
    }

    id_number = find_from_name(database=DEFAULT_DB, name=name)
    print(id_number)

    # if not(id_number is None):
    #     recipe_dict['id']=id_number

    # print(recipe_dict)


    # for k in keys:
    #     print(k,recipe_dict[k])

    str_k_list = '('

    for k in keys:
        str_k_list += f'{k}, '
    
    if len(id_number)>0:
        str_k_list =  str_k_list+' id )'
    else: 
        str_k_list = str_k_list[:-2]+')'

    if len(id_number)>0:
        recipe_dict['id'] = id_number[0][0]
        
    tuple_vals = tuple(recipe_dict[k] for k in recipe_dict.keys())
    print(tuple_vals)
    nvals = len(tuple_vals)
    qmark = nvals*'?, '
    str_var = f'({qmark[:-2]})'
    print(str_var)

        # tuple_names = (f"{k}" for k in recipe_dict.keys())
        # tuple
    sql_str = f"insert or replace into Recipes{str_k_list} values {str_var}"
    print(sql_str)
    c.execute(sql_str, 
            tuple_vals)   
    # else: 
    #     c.execute(f"insert into Recipes( {k}) values (?)", 
    #             (recipe_dict[k],))


    # str_k_list = ''
    # val_str  = ''
    # for k in keys:
    #     str_k_list += f' {k}, '
    #     val_str += f"'{recipe_dict[k]}', "
        
    # print(str_k_list)
    # print(val_str)
    
    # # # sql = 'INSERT INTO Recipes(name, servings, source) VALUES("Pasta with bacon and tomato sauce", 3, "Arthur Ngondo")'
    # # sql = f"insert into Recipes(?) values (?)", (str_k_list[:-2],val_str[:-2],)
    # sql = f'INSERT INTO Recipes({str_k_list[:-2]}) VALUES({val_str[:-2]})'

    # print(sql)

    # c.execute(sql)


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

    print(name)
    c.execute(f"SELECT id from Recipes WHERE name=(?)", (name,))
    ids = c.fetchall()

    return ids

def delete_recipe(database=DEFAULT_DB, name=None, id=None):

    conn = sqlite3.connect(database)
    c = conn.cursor()

    if not(name is None):
        c.execute(f"DELETE from Recipes WHERE name=(?)",name)

    if not(id is None):
        c.execute("DELETE from Recipes WHERE id=(?)",(id,))

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
    c.execute(f"SELECT * from Recipes WHERE name=(?)",(name,))
    recipe_dict = c.fetchone()

    return recipe_dict


def modify_recipe(database= DEFAULT_DB, name=None, keys_modify = [], values=[]):

    

    conn = sqlite3.connect(database)
    c = conn.cursor()


    # Find which line
    c.execute(f"SELECT * from Recipes WHERE name=(?)", (name,))
    rows = c.fetchone()
    print(rows)



    # AJOUTER GARDE-FOU RECETTE AVEC PLUSIEURS NOMS

    for i, k in enumerate(keys_modify):

        if type(values[i]) == str:
            update_statement = f"UPDATE Recipes SET {k}='{values[i]}' WHERE name ='{name}'"
        else: 
            update_statement = f"UPDATE Recipes SET {k}={values[i]} WHERE name ='{name}'"

        c.execute(update_statement)

    c.execute(f"SELECT * from Recipes WHERE name=(?)", (name,))
    rows = c.fetchone()
    print(rows)

    conn.commit()

def extract_ingredients(content):
   
    # Find all the lines that start with a hyphen, followed by some content
    lines = re.findall(r'-\s*([^-\n]+)', content)
    
    # Process each line to remove quantities (anything before 'of' or numbers)
    ingredients = []
    for line in lines:
        # Remove quantities, units, and the word "of"
        ingredient = re.sub(r'(\d+(\.\d+)?\s*\w*\s*|\s*(de|d\')\s*)', '', line).strip()
        ingredients.append(ingredient)

    return ingredients

def extract_title(content):

    title = re.sub(r'(#\s*)', '', content).strip()
    return title

def add_from_md(md_path, regime):

    ### NOT CLEAR IF HERE OR IN WRITE RECIPE
    if not(md_path is None):

        recipe_md = open(md_path, 'r').read()

        sections = recipe_md.split("\n## ")

        title = extract_title(sections[0])

        ingredient_st = sections[1].strip()
        ingredient_list = extract_ingredients(ingredient_st)


        recipe_dict = {
            'name':title,
            'cookbook':md_path,
            'page':None,
            'regime':regime,
        }

        if len(ingredient_list)<=4:
            for i in range(len(ingredient_list)):
                recipe_dict[f'ingredient_{i+1}']=ingredient_list[i]

            for i in range(len(ingredient_list),4):
                recipe_dict[f'ingredient_{i+1}']=''
            recipe_dict["other_ingredients"]=''

        else: 
            for i in range(0,4):
                recipe_dict[f'ingredient_{i+1}']=ingredient_list[i]
            
            other_str = ''
            for i in range(4,len(ingredient_list)):
                other_str += f"{ingredient_list[i]}, "

        add_recipe(database=DEFAULT_DB, **recipe_dict)



        # return title, ingredient_list

