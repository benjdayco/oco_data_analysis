import pandas as pd
import numpy as np
from pandasql import sqldf

coms_projects = pd.read_csv("data_files/all_coms_projects_copy.csv")
cofin_projects = pd.read_csv("data_files/cofin_grant_loans_clean_approval_no.csv", encoding='utf-8')

#reformat approval number as 4 character string instead of int
coms_projects['approval_number'] = coms_projects['approval_number'].astype(str)
coms_projects['approval_number'] = coms_projects['approval_number'].apply(lambda x: x.zfill(4))

#reformat approval number as 4 character string instead of int
cofin_projects['approval_number'] = cofin_projects['approval_number'].astype(str)
cofin_projects['approval_number'] = cofin_projects['approval_number'].apply(lambda x: x.zfill(4))

#set coms approval number as index
coms_projects = coms_projects.set_index(['approval_number'])

#add cofin fields
cofin_projects['coms_proj_no'] = ""
cofin_projects['coms_project_title'] = ""

for index,row in cofin_projects.iterrows():

	approval_number = str(row['approval_number'])

	#temporary store approval number of current row
	try:
		proj_no = coms_projects.loc[approval_number]["proj_no"]
		project_title = coms_projects.ix[approval_number,"project_title"]
		print proj_no, project_title
		cofin_projects.ix[index,"coms_proj_no"] = "hello" 
		cofin_projects.ix[index, "coms_project_title"] = "hello"
	except KeyError:	
		cofin_projects.ix[index,"coms_proj_no"] = "not in CoMs"
		cofin_projects.ix[index, "coms_project_title"] = "not in CoMs"