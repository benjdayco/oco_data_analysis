import pandas as pd
import numpy as np

cofin_coms_projects_sample = pd.read_csv("data_files/cofin_coms_project_relationship_sample.csv", encoding='utf-8')

#reformat approval number as 4 character string instead of int
cofin_coms_projects_sample['approval_number'] = cofin_coms_projects_sample['approval_number'].astype(str)
cofin_coms_projects_sample['approval_number'] = cofin_coms_projects_sample['approval_number'].apply(lambda x: x.zfill(4))

cofin_coms_projects_sample = cofin_coms_projects_sample.set_index(['approval_number'])

#cofin_projects_not_in_coms_sample = cofin_coms_projects_sample.loc[cofin_coms_projects_sample.coms_proj_no == "not in CoMs"]

#extract records that are in cofin but not in coms
cofin_projects_not_in_coms_sample = cofin_coms_projects_sample[cofin_coms_projects_sample.coms_proj_no == "not in CoMs"]
cofin_projects_not_in_coms_sample.to_csv('data_files/cofin_projects_not_in_coms_sample.csv')

#extract records that are in cofin with different proj no in comes
cofin_projects_in_coms_sample = cofin_coms_projects_sample[cofin_coms_projects_sample.coms_proj_no != "not in CoMs"]
cofin_projects_diff_proj_no_coms_sample = cofin_projects_in_coms_sample[(cofin_projects_in_coms_sample.proj_no != cofin_projects_in_coms_sample.coms_proj_no)]
cofin_projects_diff_proj_no_coms_sample.to_csv('data_files/cofin_projects_diff_proj_no_coms_sample.csv')