import pandas as pd
import numpy as np

cofin_grants_loan_data = pd.read_csv("data_files/cofin_grants_loans.csv")

cofin_grants_loan_sample = cofin_grants_loan_data.loc[cofin_grants_loan_data['Loan Grant Number']  == '9115' ]

print cofin_grants_loan_sample

cofin_grants_loan_sample.to_csv("data_files/cofin_grants_loan_sample.csv")
