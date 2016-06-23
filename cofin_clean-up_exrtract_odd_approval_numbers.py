import pandas as pd
import numpy as np

cofin_grants_loans_data = pd.read_csv("data_files/cofin_grant_loans_2007_clean_proj_no.csv")

#remove records with all blank columns (noise from lotus notes)
#cofin_grants_loans_proc_data = cofin_grants_loans_data_raw.dropna(subset = ['Approval Numbers CoFin','Proj No'] , how='all')

# print summary of null fields
#print cofin_grants_loans_proc_data.isnull().sum()

#extract all records with null project numbers
#print len(cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].isnull()])
#cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].isnull()].to_csv("data_files/cofin_grant_loans_null_proj_no.csv")

#extract all records with 5 digit project numbers
#print len(cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].str.len() == 5])
#cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].str.len() == 5].to_csv("data_files/cofin_grant_loans_short_proj_no.csv")

#extract all records with odd formated approval numbers project numbers
print cofin_grants_loans_data[cofin_grants_loans_data['Extracted Approval Number'].str.len() != 4]
cofin_grants_loans_data[cofin_grants_loans_data['Extracted Approval Number'].str.len() != 4].to_csv("data_files/cofin_grant_loans_odd_approval_no.csv")
