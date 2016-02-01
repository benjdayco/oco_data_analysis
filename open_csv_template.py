import pandas as pd
import numpy as np

all_psc_data = pd.read_csv("./data_files/all_psc.csv")

print all_psc_data.loc[['approval number'], ['title']]




