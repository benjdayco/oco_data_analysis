import pandas as pd
import numpy as np

cofin_grants_loan_2007 = pd.read_csv("data_files/cofin_grants_loan_from_2007.csv")

with_slash = cofin_grants_loan_2007[cofin_grants_loan_2007['Loan Grant No'].str.contains("/")]

with_slash.to_csv("data_files/cofin_grants_loan_from_2007_with_slash.csv")

print with_slash