import pandas as pd
import numpy as np

cofin_grants_loans_data_raw = pd.read_csv("data_files/cofin loan grants with year-2-18-2016.csv")

#remove records with all blank columns (noise from lotus notes)
cofin_grants_loans_proc_data = cofin_grants_loans_data_raw.dropna(subset = ['Approval Numbers CoFin','Proj No'] , how='all')

# print summary of null fields
print cofin_grants_loans_proc_data.isnull().sum()

#extract all records with null project numbers
#print len(cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].isnull()])
#cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].isnull()].to_csv("data_files/cofin_grant_loans_null_proj_no.csv")

#extract all records with 5 digit project numbers
#print len(cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].str.len() == 5])
#cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].str.len() == 5].to_csv("data_files/cofin_grant_loans_short_proj_no.csv")

#extract all records with odd formated approval numbers project numbers
cofin_grants_loans_proc_data.to_csv("data_files/cofin_grant_loans_clean.csv")
