import pandas as pd
import numpy as np

cofin_ta_data = pd.read_csv("data_files/cofin_ta.csv")

cofin_ta_2007 = cofin_ta_data.loc[cofin_ta_data.Year >= 2007]

print cofin_ta_2007

cofin_ta_2007.to_csv("data_files/cofin_ta_from_2007.csv")

