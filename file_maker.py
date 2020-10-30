import numpy as np
import pandas as pd
import csv
import os

index_df = pd.read_csv('posts_index.csv',  sep=',', encoding='utf-8', engine='python')

print("\nPosts index: ")

entries = os.listdir('./posts')

full_df = pd.DataFrame(data=None)

for entry in entries:
	entry = "./posts/" + entry
	print(entry)
	df = pd.read_csv(entry,  sep=',', encoding='utf-8', engine='python', usecols=['URL','Message','Image Text','Link Text', 'Description'])
	merged_data = index_df.merge(df,on=['URL'])
	full_df = full_df.append(merged_data, ignore_index = True)

print(full_df)
full_df.to_csv(r'selectedPosts.csv')