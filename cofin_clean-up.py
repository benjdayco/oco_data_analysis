import pandas as pd
import numpy as np

cofin_grants_loan_data_raw = pd.read_csv("data_files/data_dump_cofinanced_loans-grants.csv")

cofin_grants_loan_data = cofin_grants_loan_data_raw.dropna(subset = ['Approval Number','Proj No', "Country Mnemonic"d,'Loan/Grant Title', Approval Numbers,Proj No,Country Mnemonic,Loan/Grant Title,Department,Division,Approval,OCR,ADF Loan,ADF Grant,SF,Total,Grants,Loans,Commercial,Total CF] , how='all')

cofin_grants_loan_subset = cofin_grants_loan_data[['Partner', 'Approval Numbers', 'Proj No', 'Loan/Grant Title']]



print cofin_grants_loan_data




