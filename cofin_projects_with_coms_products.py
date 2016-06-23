#List Products by Project Number with equivalent project number in CoMs per Products
#input: "data_files/cofin_coms_relationship_by_approval_number.csv" produce by cofin_coms_project_relationship.csv
#		"data_files/cofin_grants_loans_data_for_coms.csv"" formated by cofin_clean_up_prepare_for_coms_comparison.py
#output: "data_files/cofin_coms_relationship_by_project_number.csv" produce by cofin_coms_by_project_number.csv

import pandas as pd
import numpy as np

#read data files
#
cofin_coms_projects = pd.read_csv("data_files/cofin_coms_project_relationship_sample.csv")
cofin_projects = pd.read_csv("data_files/cofin_grants_loans_data_for_coms.csv", encoding='utf-8')

#initialize output dataframe
cofin_projects_with_coms = cofin_projects
cofin_projects_with_coms['coms_proj_no'] = ""
cofin_projects_with_coms['coms_proj_title'] = ""

#reformat approval number as 4 character string instead of int
cofin_coms_projects['approval_number'] = cofin_coms_projects['approval_number'].astype(str)
cofin_coms_projects['approval_number'] = cofin_coms_projects['approval_number'].apply(lambda x: x.zfill(4))


#reformat approval number as 4 character string instead of int
cofin_projects['approval_number'] = cofin_projects['approval_number'].astype(str)
cofin_projects['approval_number'] = cofin_projects['approval_number'].apply(lambda x: x.zfill(4))

#create temporary dataframe for coms fields
coms_project_fields = pd.DataFrame()

#iterate on each row of cofin_projects
for index,row in cofin_projects.iterrows():

	#extract approval number of row
	cofin_approval_number = row['approval_number']

	#select coms project number [from cofin_coms_projects by approval number
	coms_proj_row = cofin_coms_projects[cofin_coms_projects.approval_number == cofin_approval_number]
	
	coms_project_fields = coms_project_fields.append(coms_proj_row, ignore_index=True)

	cofin_projects_with_coms['coms_proj_no'] = coms_project_fields['coms_proj_no']
	cofin_projects_with_coms['coms_project_title'] = coms_project_fields['coms_project_title']


cofin_projects_with_coms = cofin_projects_with_coms.set_index(['proj_no', 'approval_number'])

print cofin_projects_with_coms


cofin_projects_with_coms.to_csv("data_files/cofin_coms_relationship_by_project_number.csv", encoding='utf-8')

xl_writer = ExcelWriter('cofin_coms_relationship_by_project_number.xlsx') 

cofin_projects_with_coms.to_csv(writer, sheet2)

