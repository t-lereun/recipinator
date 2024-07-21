import sqlite3
from init_database import keys



def add_recipe(name=None, cookbook=None, page=None, 
               ingredient_1=None, ingredient_2=None,
               ingredient_3=None, ingredient_4=None,
               other_ingredients=None):
    
    conn = sqlite3.connect("./recipes/recipes.db")
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

