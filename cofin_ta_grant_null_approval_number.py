import pandas as pd
import numpy as np

cofin_grants_loan_data = pd.read_csv("data_files/data_dump_cofinanced_loans-grants.csv")

#cofin_grants_loan_2007 = cofin_grants_loan_data.loc[cofin_grants_loan_data.Year >= 2007]

#null_approval = cofin_grants_loan_2007['Approval Numbers'].isnull()

#cofin_grants_loan_2007_with_null_fields = cofin_grants_loan_2007.loc[cofin_grants_loan_2007['with empty'] == False]

#print "total number of rows: " + str(len(cofin_grants_loan_2007))
#print "total number of rows with empty fields: " + str(len(cofin_grants_loan_2007_with_empty_fields))

print cofin_grants_loan_data.columns



