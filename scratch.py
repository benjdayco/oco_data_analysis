import pandas as pd
import numpy as np

df = pd.read_csv("data_files/test_data.csv")
temp_df = pd.DataFrame()
count = 0

for index, row in df.iterrows():
	count = count + 1
	new_row = row
	new_row['new col'] = count
	
	temp_df = temp_df.append(new_row, ignore_index=True)
	new_df = temp_df

print new_df
	


 