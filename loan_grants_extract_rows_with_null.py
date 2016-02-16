import pandas as pd
import numpy as np

cofin_grants_loan_2007 = pd.read_csv("data_files/cofin_grants_loan_from_2007.csv")

with_empty = cofin_grants_loan_2007.isnull().any(axis=1)

cofin_grants_loan_2007['with empty'] = with_empty

cofin_grants_loan_2007_with_empty_fields = cofin_grants_loan_2007.loc[cofin_grants_loan_2007['with empty'] == False]

print "total number of rows: " + str(len(cofin_grants_loan_2007))
print "total number of rows with empty fields: " + str(len(cofin_grants_loan_2007_with_empty_fields))

cofin_grants_loan_2007_with_empty_fields.to_csv("data_files/cofin_grants_loan_from_2007_without_null.csv")