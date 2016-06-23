import pandas as pd
import numpy as np

coms_projects = pd.read_csv("data_files/all_coms_projects_copy.csv")
cofin_projects = pd.read_csv("data_files/cofin_grant_loans_clean_approval_no_2007.csv", encoding='utf-8')

coms_projects = coms_projects.sort_values(by=['proj_no'])
cofin_projects = cofin_projects.sort_values(by=['proj_no'])

#reformat approval number as 4 character string instead of int
cofin_projects['approval_number'] = cofin_projects['approval_number'].astype(str)
cofin_projects['approval_number'] = cofin_projects['approval_number'].apply(lambda x: x.zfill(4))

#reformat approval number as 4 character string instead of int
coms_projects['approval_number'] = coms_projects['approval_number'].astype(str)
coms_projects['approval_number'] = coms_projects['approval_number'].apply(lambda x: x.zfill(4))

cofin_projects_stacked = cofin_projects.set_index(['proj_no','approval_number'])

coms_projects_stacked = coms_projects.set_index(['proj_no', 'approval_number'])

print cofin_projects_stacked