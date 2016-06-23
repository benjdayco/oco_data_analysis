import pandas as pd
import numpy as np

cofin_grants_loans_data = pd.read_csv("data_files/cofin_grant_loans_2007_clean_proj_no.csv")


#extract all records with odd formated approval numbers project numbers
#print cofin_grants_loans_data[cofin_grants_loans_data['Extracted Approval Number'].str.len() == 4]
#cofin_grants_loans_data[cofin_grants_loans_data['Extracted Approval Number'].str.len() == 4].to_csv("data_files/cofin_grant_loans_clean_approval_no.csv")

print cofin_grants_loans_data.sort(['Year'])