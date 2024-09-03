import pandas as pd
from sources.init_database import keys
import os
from pathlib import Path
import numpy as np
from sources import common

ingredient_keys = ['ingredient_1','ingredient_2','ingredient_3','ingredient_4','other_ingredients']

def get_full_ingredient_list(df):
    

    df['full ingredient list'] = ''
    for k in ingredient_keys:
        df['full ingredient list'] += df[k] + ','

    return df


def filter(df, filter=None):
     
    # Open filter
    if not(filter is None):
        dbdir = os.path.join(Path(__file__).parents[1],'filters',filter)
        forbidden = np.genfromtxt(dbdir,dtype=str)
        filter_key = filter
        df[filter_key] = True

        for i, row in df.iterrows():
            full_ingredient_list = ''
            for k in ingredient_keys:
                full_ingredient_list += df.loc[i,k] + ','
            full_ingredient_list = full_ingredient_list[:-1]


            list_ingredients = full_ingredient_list.split(',')
            # print(list_ingredients)
            for j, l in enumerate(list_ingredients):
                l = l.strip()
                if l in forbidden:
                    df.loc[i,filter_key] = False

        c1 = 'background-color: none'
        c2 = 'background-color: green'
        d = {"False":c1,"True":c2}

        df.style.apply(lambda x: x[filter_key].map(d))
        

        return df[df[filter_key]==True]

    

def filter_by_ingredient(df, ingredient=None):

    if not(ingredient is None):


        filter_key = ingredient
        df[filter_key] = False

        for i, row in df.iterrows():
            full_ingredient_list = ''
            for k in ingredient_keys:
                print(df.loc[i,k])
                full_ingredient_list += df.loc[i,k] + ','
            full_ingredient_list = full_ingredient_list[:-1]

            list_ingredients = full_ingredient_list.split(',')
            for j, l in enumerate(list_ingredients):
                l = l.strip()
                if ingredient in l:
                    df.loc[i,filter_key] = True

        res =  df[df[filter_key]==True]

    else:
        res = df

    return res

def scrap_ingredients(db_name):

    if not(db_name is None): 


        # Atm, use a dataframe to process the recipes
        df = common.db_to_df(db_name)
        full_ingredient_list = []

        for i, row in df.iterrows():
            ingredients_string = ''
            for k in ingredient_keys:
                ingredients_string += df.loc[i,k] + ','
            ingredients_string = ingredients_string[:-1]
            print("string", ingredients_string)

            list_ingredients = ingredients_string.split(',')
            list_ingredients = [l.strip() for l in list_ingredients]
            print("full ing", full_ingredient_list)
            print(list_ingredients)

            full_ingredient_list.extend(list_ingredients)
        
        full_ingredient_list = np.asarray(full_ingredient_list)

        return np.unique(full_ingredient_list)
    
    else:
        pass





        





