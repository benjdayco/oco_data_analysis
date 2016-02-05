import pandas as pd
import numpy as np

cofin_ta_2007 = pd.read_csv("data_files/cofin_ta_from_2007.csv")

with_empty = cofin_ta_2007.isnull().any(axis=1)

cofin_ta_2007['with empty'] = with_empty

cofin_ta_2007_with_empty_fields = cofin_ta_2007.loc[cofin_ta_2007['with empty'] == True]


cofin_ta_2007_with_empty_fields.to_csv("data_files/cofin_ta_from_2007_with_null.csv")
print "total number of rows: " + str(len(cofin_ta_2007))
print "total number of rows with empty fields: " + str(len(cofin_ta_2007_with_empty_fields))

