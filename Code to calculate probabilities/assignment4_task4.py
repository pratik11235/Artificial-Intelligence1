# -*- coding: utf-8 -*-
"""
Created on Sun May  1 16:01:58 2022

@author: Pratik Antoni Patekar
"""

import pandas as pd
import sys

# Function to calculate the prior probabilities
def calc_prior_prob(df, var_name):
    p1 = len(df[df[var_name] == '1'])/ len(df[var_name])
    return p1

# Function to calculate the conditional probability of a variable
# for 2 or 3 given variables
def calc_cond_prob(df, var_name, given_var_name1, given_var_name2 = 'any'):
    if given_var_name2 == 'any':
        p1 = (len(df[(df[given_var_name1] == '1') & (df[var_name] == '1')]))/(len(df[df[given_var_name1] == '1']))
        p2 = (len(df[(df[given_var_name1] == '0') & (df[var_name] == '1')]))/(len(df[df[given_var_name1] == '0']))
        return p1, p2
    else:
        p1 = (len(df[(df[given_var_name1] == '1') & (df[given_var_name2] == '1') & (df[var_name] == '1')]))/(len(df[(df[given_var_name1] == '1') & (df[given_var_name2] == '1')]))
        p2 = (len(df[(df[given_var_name1] == '0') & (df[given_var_name2] == '1') & (df[var_name] == '1')]))/(len(df[(df[given_var_name1] == '0') & (df[given_var_name2] == '1')]))
        p3 = (len(df[(df[given_var_name1] == '1') & (df[given_var_name2] == '0') & (df[var_name] == '1')]))/(len(df[(df[given_var_name1] == '1') & (df[given_var_name2] == '0')]))
        p4 = (len(df[(df[given_var_name1] == '0') & (df[given_var_name2] == '0') & (df[var_name] == '1')]))/(len(df[(df[given_var_name1] == '0') & (df[given_var_name2] == '0')]))
        return p1, p2, p3, p4

# Read file contents and store them in pandas dataframe with required headers
headers = ['baseball_game_on_TV', 'George_watches_TV', 'out_of_cat_food', 'George_feeds_cat']
data = []
try:
    with open('training_data.txt', 'r') as f:
        line = f.readline().rstrip('\n')
        data.append(line.split('     ')[1:])
        while line:
            line = f.readline().rstrip('\n')
            if line != "":
                data.append(line.split('     ')[1:])
except:
    print("Unable to open the file.")
    print("Please check if the training_data.txt file is present in the same path as the source code.")
    sys.exit()
    
df = pd.DataFrame(data, columns = headers)
print("Following the data from the training file:")
print(df)

# Function call to find the prior probabilities
p1 = calc_prior_prob(df, 'baseball_game_on_TV')
print('P(baseball_game_on_TV) =', p1)
p2 =  calc_prior_prob(df, 'out_of_cat_food')
print('P(out_of_cat_food) =', p2)
print("\n")

# Function call to calculate the conditional probabilities
p3, p4 = calc_cond_prob(df, 'George_watches_TV', 'baseball_game_on_TV')
print('P(George_watches_TV = True | baseball_game_on_TV = True) =', p3, '\nP(George_watches_TV = False | baseball_game_on_TV = True) =', 1-p3)
print('P(George_watches_TV = True | baseball_game_on_TV = False) =', p4, '\nP(George_watches_TV = False | baseball_game_on_TV = False) =', 1-p4)
print('\n')
p5, p6, p7, p8 = calc_cond_prob(df, 'George_feeds_cat', 'George_watches_TV', 'out_of_cat_food')
print('P(George_feeds_cat = True | (George_watches_TV = True , out_of_cat_food = True))) = ', p5)
print('P(George_feeds_cat = False | (George_watches_TV = True , out_of_cat_food = True))) = ', 1-p5)
print('P(George_feeds_cat = True | (George_watches_TV = False , out_of_cat_food = True))) = ', p6)
print('P(George_feeds_cat = False | (George_watches_TV = False , out_of_cat_food = True))) = ', 1-p6)
print('P(George_feeds_cat = True | (George_watches_TV = True , out_of_cat_food = False))) = ', p7)
print('P(George_feeds_cat = False | (George_watches_TV = True , out_of_cat_food = False))) = ', 1-p7)
print('P(George_feeds_cat = True | (George_watches_TV = False , out_of_cat_food = False))) = ', p8)
print('P(George_feeds_cat = False | (George_watches_TV = False , out_of_cat_food = False))) = ', 1-p8)



