import pandas as pd
import numpy as np

cofin_grants_loan_data = pd.read_csv("data_files/cofin_grant_loans_clean.csv")

cofin_grants_loan_2007 = cofin_grants_loan_data.loc[cofin_grants_loan_data.Year >= 2007]

print cofin_grants_loan_2007.sort(['Year'])

#cofin_grants_loan_2007.to_csv("data_files/cofin_grants_loan_from_2007.csv")

cofin_grants_loan_data