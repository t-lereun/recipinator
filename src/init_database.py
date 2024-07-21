import sqlite3


keys = ['name', 'cookbook', 'page', 'ingredient_1','ingredient_2', 'ingredient_3', 'ingredient_4', 'other_ingredients']
dtype = {
    'name':'TEXT',
    'cookbook':'TEXT',
    'page':'INTEGER',
    'ingredient_1':'TEXT',
    'ingredient_2':'TEXT',
    'ingredient_3':'TEXT',
    'ingredient_4':'TEXT',
    'other_ingredients':'TEXT',
    }

def init_database():


    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()

    # create Recipe table - Holds gross recipe information
    str_list = ''
    for k in keys:
        str_list += f'{k} {dtype[k]}, '

    sql =f'CREATE TABLE Recipes(id INTEGER PRIMARY KEY, {str_list[:-2]} )'
    print(sql)
    c.execute(sql)

        # sql = f"CREATE TABLE IF NOT EXISTS {k} "
        # sql += f"([id] INTEGER PRIMARY KEY, {k} {dtype[k]})"
        # print(sql)

        # c.execute(sql)


    conn.commit()

    my_recipe = {
        'name':'Toad-in-the-hole',
        'cookbook':'OTK',
        'page':'106',
        'ingredient_1':'céleri-rave',
        'ingredient_2':'betterave',
        'ingredient_3':'farine',
        'ingredient_4':'oeuf',
        'other_ingredients':"sirop érable, lait, moutarde, rutabaga",
        }

    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()


    str_k_list = ''
    val_str  = ''
    for k in keys:
        str_k_list += f' {k}, '
        val_str += f"'{my_recipe[k]}', "
            

        
    # sql = 'INSERT INTO Recipes(name, servings, source) VALUES("Pasta with bacon and tomato sauce", 3, "Arthur Ngondo")'
    sql = f'INSERT INTO Recipes({str_k_list[:-2]}) VALUES({val_str[:-2]})'

    print(sql)

    c.execute(sql)


    conn.commit()

if __name__=='__main__':
    init_database()


# c.execute(
#     """
#     INSERT INTO recipe_name (recipe_id, recipe_name)
#     VALUES
#     (1,'Toad-in-the-hole riche en légumes')
#     """
# )

# c.execute(
#     """
#     INSERT INTO recipe_name (recipe_id, cook_book)
#     VALUES
#     (1, 'Ottolenghi test kitchen')
#     """
# )

# conn.commit()

