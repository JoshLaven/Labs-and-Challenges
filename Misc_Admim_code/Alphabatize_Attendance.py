import pandas as pd 
import os

path = '~Sarah/Downloads'
filename = 'participants_840148924.csv'

df = pd.read_csv(os.path.join(path, filename))
#investigate
df.columns
df.shape
type(df['Name (Original Name)'][0])

df = df[df['Total Duration (Minutes)'] > 5]


sorted(df['Name (Original Name)'], key=lambda x: x.split(" ")[-1])
#cite https://chrisalbon.com/python/basics/sort_a_list_by_last_name/