import pandas as pd
import numpy as np

cofin_grants_loan_2007 = pd.read_csv("data_files/cofin_grants_loan_from_2007.csv")

print cofin_grants_loan_2007.count()

print cofin_grants_loan_2007.describe()
