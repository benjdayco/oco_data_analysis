import pandas as pd
import numpy as np

df = pd.read_csv("data_files/test_data.csv")
temp_df = pd.DataFrame()
count = 0

for index, row in df.iterrows():
	new_row = row
	string = row['String']
	string_split =  string.split("/")

	for new_string in string_split:
		new_row['String'] = new_string
		temp_df = temp_df.append(new_row, ignore_index=True)
		new_df = temp_df

print new_df
	


 