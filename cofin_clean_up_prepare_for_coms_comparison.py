#Prepare CoFin data dump prepared for comparison with CoMs
#Produces "data_files/cofin_grants_loans_data_for_coms.csv"

import pandas as pd
import numpy as np

#read raw CoFin Data Dump
cofin_grants_loans_data = pd.read_csv("data_files/cofin_grant_loans_clean.csv")

#create dataframe for file output
cofin_grants_loans_data_for_coms = pd.DataFrame()

#extract all 2007 to present from data set with extracted approval numbers
cofin_grants_loans_2007 = cofin_grants_loans_data.loc[cofin_grants_loans_data.Year >= 2007]

#update output dataframe
cofin_grants_loans_data_for_coms = cofin_grants_loans_2007

#
#separate approval numbers numbers
#
#createtemporary dataframe 
temp_df = pd.DataFrame()

#create dataframe with only Partner, Approval Numbers, Proj. No, and Loan/Grant Title column"
cofin_grants_loans_data_short = cofin_grants_loans_data_for_coms[['Partner', 'Year', 'Approval Numbers CoFin', 'Proj No', 'Loan/Grant Title']]

#iterate each row
for index,row in cofin_grants_loans_data_short.iterrows():
	#temporary store approval number of current row
	approval_number_orig = str(row['Approval Numbers CoFin'])

	#split approval number into array by character "/""
	approval_number_split =  approval_number_orig.split("/")
	
	#itererate through each approval number in array
	for number in approval_number_split:
		
		new_row = row #store new row in temporary Series
		new_row['Extracted Approval Number'] = number #add number as new column
		
		#insert current approval number into new dataframe with row[Project No]
		temp_df = temp_df.append(new_row, ignore_index=True)
		new_df = temp_df
#update output dataframe
cofin_grants_loans_data_for_coms = new_df[['Partner', 'Year', 'Approval Numbers CoFin', 'Extracted Approval Number', 'Proj No', 'Loan/Grant Title']]

#pad trailing zeros in approval number
fill_zero = cofin_grants_loans_data_for_coms['Extracted Approval Number'].apply(lambda x: x.zfill(4))
cofin_grants_loans_data_for_coms['Extracted Approval Number'] = fill_zero

#remove approval numbers with different format from CoMs
cofin_grants_loans_data_clean_approval_number = cofin_grants_loans_data_for_coms[cofin_grants_loans_data_for_coms['Extracted Approval Number'].str.len() == 4]
cofin_grants_loans_data_for_coms = cofin_grants_loans_data_clean_approval_number

#remove odd project numbers with different format from CoMs
#records with 5 digit project numbers
cofin_grants_loans_clean_proj_no = cofin_grants_loans_data_for_coms[cofin_grants_loans_data_for_coms['Proj No'].str.len() == 9]
cofin_grants_loans_data_for_coms = cofin_grants_loans_clean_proj_no

#write data set
print cofin_grants_loans_data_for_coms
cofin_grants_loans_data_for_coms.to_csv("data_files/cofin_grants_loans_data_for_coms.csv")
print "File Output: data_files/cofin_grants_loans_data_for_coms.csv"
