import pandas as pd
from sources.init_database import keys
import os
from pathlib import Path
import numpy as np
from sources import common
from sources.streamlit_toolkit import seasons
import yaml

ingredient_keys = ['ingredient_1','ingredient_2','ingredient_3','ingredient_4','other_ingredients']

SEASONS_PATH = os.path.join(common.ROOT,'filters','seasons.yml')



with open(SEASONS_PATH,'r') as file:
    SEASONS = yaml.safe_load(file)
file.close()

ALL_ING = []
for month in SEASONS:
    ALL_ING.extend(SEASONS[month])

ALL_ING = [s.lower() for s in ALL_ING]



def get_full_ingredient_list(df):
    

    df['full ingredient list'] = ''
    for k in ingredient_keys:
        df['full ingredient list'] += df[k] + ','

    return df

def filter_by_diet(df, diet=None):

    res = df
    if not diet==None:
        res = df[df['regime']==diet]

    return res


def get_ingredient_list(df, i):

    full_ingredient_list = ''
    for k in ingredient_keys:
        full_ingredient_list += df.loc[i,k] + ','
    full_ingredient_list = full_ingredient_list[:-1]

    return full_ingredient_list.split(',')




def score_by_season(df):

    month = seasons.get_month()
    season_list = SEASONS[month]
    season_list = [s.lower() for s in season_list]

    for i, row in df.iterrows():
        
        list_ingredients = get_ingredient_list(df, i )

        season_score = 0

        for l in list_ingredients:
            if l in ALL_ING:
                if l in season_list:
                    print("saison",l)
                    season_score += 1
                else: 
                    print(l)
                    season_score += -1

        df.loc[i,"season score"] = season_score

    df = df.sort_values("season score", ascending=False)

    return df



    




        


# def filter(df, filter=None):
     
#     # Open filter
#     if not(filter is None):
#         dbdir = os.path.join(Path(__file__).parents[1],'filters',filter)
#         forbidden = np.genfromtxt(dbdir,dtype=str)
#         filter_key = filter
#         df[filter_key] = True

#         for i, row in df.iterrows():
#             full_ingredient_list = ''
#             for k in ingredient_keys:
#                 full_ingredient_list += df.loc[i,k] + ','
#             full_ingredient_list = full_ingredient_list[:-1]


#             list_ingredients = full_ingredient_list.split(',')
#             # print(list_ingredients)
#             for j, l in enumerate(list_ingredients):
#                 l = l.strip()
#                 if l in forbidden:
#                     df.loc[i,filter_key] = False

#         c1 = 'background-color: none'
#         c2 = 'background-color: green'
#         d = {"False":c1,"True":c2}

#         df.style.apply(lambda x: x[filter_key].map(d))
        

#         return df[df[filter_key]==True]

    

def filter_by_ingredient(df, ingredient=None):

    if not(ingredient is None):


        filter_key = ingredient
        df[filter_key] = False

        for i, row in df.iterrows():
            list_ingredients = get_ingredient_list(df, i)
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
            # print("string", ingredients_string)

            list_ingredients = ingredients_string.split(',')
            list_ingredients = [l.strip() for l in list_ingredients]
            # print("full ing", full_ingredient_list)
            # print(list_ingredients)

            full_ingredient_list.extend(list_ingredients)
        
        full_ingredient_list = np.asarray(full_ingredient_list)

        return np.unique(full_ingredient_list)
    
    else:
        pass





        





