import pandas as pd
import numpy as np

cofin_ta_2007 = pd.read_csv("data_files/cofin_ta_from_2007.csv")

print "total number of rows: " + str(len(cofin_ta_2007))
print "Column Count"
print cofin_ta_2007.count()
