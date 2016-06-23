#Extract CoFin Records with Project Numbers that matches the CoMs format from 2007 to Present
#Produces "data_files/cofin_grant_loans_2007_clean_proj_no.csv"

import pandas as pd
import numpy as np

#import data file
cofin_grants_loans_data_raw = pd.read_csv("data_files/cofin_grants_extracted_approval_numbers.csv")

#remove records with all blank columns (noise from lotus notes)
cofin_grants_loans_proc_data = cofin_grants_loans_data_raw.dropna(subset = ['Approval Numbers CoFin','Proj No'] , how='all')

#extract all records with null project numbers
cofin_grant_loans_with_proj_no = cofin_grants_loans_proc_data[cofin_grants_loans_proc_data['Proj No'].notnull()]

#extract all records with 5 digit project numbers
cofin_grant_loans_clean_proj_no = cofin_grant_loans_with_proj_no[cofin_grant_loans_with_proj_no['Proj No'].str.len() == 9]

#extract all records from 2007 to Present
cofin_grant_loans_2007_clean_proj_no = cofin_grant_loans_clean_proj_no.loc[cofin_grant_loans_clean_proj_no.Year >= 2007]
print cofin_grant_loans_2007_clean_proj_no

#write to file
#cofin_grant_loans_2007_clean_proj_no.to_csv("data_files/cofin_grant_loans_2007_clean_proj_no.csv")

print cofin_grant_loans_2007_clean_proj_no.sort(['Year'])