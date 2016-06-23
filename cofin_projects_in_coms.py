#Produces data file that shows CoMs project number of each CoFin Approval Number
#input: "data_files/cofin_extract_for_coms_comparison.csv" formated by cofin_clean_up_prepare_for_coms_comparison.py
#output: "data_files/cofin_coms_relationship_by_approval_number.csv"

import pandas as pd
import numpy as np
from pandasql import sqldf

#read CoMs / CoFin data file
coms_projects = pd.read_csv("data_files/all_coms_projects_copy.csv")
cofin_projects = pd.read_csv("data_files/cofin_grants_loans_data_for_coms.csv", encoding='utf-8')

#reformat approval number as 4 character string instead of int
coms_projects['approval_number'] = coms_projects['approval_number'].astype(str)
coms_projects['approval_number'] = coms_projects['approval_number'].apply(lambda x: x.zfill(4))

#reformat approval number as 4 character string instead of int
cofin_projects['approval_number'] = cofin_projects['approval_number'].astype(str)
cofin_projects['approval_number'] = cofin_projects['approval_number'].apply(lambda x: x.zfill(4))

#select all distinct approval numbers from CoFin
#
q ="""
SELECT DISTINCT(approval_number), proj_no FROM cofin_projects ORDER BY approval_number
"""
cofin_project_distinct_approval_number = sqldf(q, locals())

#set-up CoMs records
#
#select grant and loans from CoMs records
coms_grant_loans = coms_projects.loc[(coms_projects['Type'] == "GRNT") | (coms_projects['Type'] == "LN")]
#set approval number as indexd
coms_grant_loans = coms_grant_loans.set_index(['approval_number'])

#
# set-up CoFIn records
#
#set approval number as index
cofin_project_distinct_approval_number = cofin_project_distinct_approval_number.set_index(['approval_number'])
#initialize blank fields for CoMs Proj No and Project Title
cofin_project_distinct_approval_number['coms_proj_no'] = ""
cofin_project_distinct_approval_number['coms_project_title'] = ""

for index,row in cofin_project_distinct_approval_number.iterrows():
	#temporary store approval number of current row
	try:
		cofin_project_distinct_approval_number.loc[index]["coms_proj_no"] = coms_grant_loans.loc[index]["proj_no"]
		cofin_project_distinct_approval_number.loc[index]["coms_project_title"] = coms_grant_loans.loc[index]["project_title"]
	except KeyError:	
		cofin_project_distinct_approval_number.loc[index]["coms_proj_no"] = "not in CoMs"
		cofin_project_distinct_approval_number.loc[index]["coms_project_title"] = "not in CoMs"

#cofin_project_distinct_approval_number["coms_proj_no"] = coms_projects["proj_no"]
print cofin_project_distinct_approval_number
cofin_project_distinct_approval_number.to_csv("data_files/cofin_coms_project_relationship_sample.csv", encoding='utf-8')
print "data saved to data_files/cofin_coms_project_relationship_sample.csv"

#cofin_prsoject_distinct_approval_number.to_csv("data_files/cofin_project_distinct_approval_number.csv", encoding='utf-8')
#print cofin_project_distinct_approval_number
cofin_project_distinct_approval_number.to_csv("data_files/cofin_coms_project_relationship_sample.csv", encoding='utf-8')


