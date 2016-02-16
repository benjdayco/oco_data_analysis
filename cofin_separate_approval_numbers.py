import pandas as pd
import numpy as np


#read data file
cofin_grants_loan_data_raw = pd.read_csv("data_files/loan_grants_test.csv")

#temporary dataframe 
temp_df = pd.DataFrame()

#remove records with all blank columns (noise from lotus notes)
cofin_grants_loan_data = cofin_grants_loan_data_raw.dropna(subset = ['Approval Numbers','Proj No'] , how='all')


#create dataframe with only Partner, Approval Numbers, Proj. No, and Loan/Grant Title column"
cofin_grants_loan_data_short = cofin_grants_loan_data[['Partner', 'Approval Numbers', 'Proj No', 'Loan/Grant Title']]
	
#iterate each row
for index,row in cofin_grants_loan_data_short.iterrows():
	#temporary store approval number of current row
	approval_number_orig = str(row['Approval Numbers'])

	#split approval number into array by character
	approval_number_split =  approval_number_orig.split("/")

	
	#itererate through each approval number in array
	for number in approval_number_split:
		
		new_row = row #store new_row in temporary Series
		new_row['indvidual approval number'] = number #add number as new column
		
		#insert current approval number into new dataframe with row[Project No]
		temp_df = temp_df.append(new_row, ignore_index=True)
		new_df = temp_df

		#print new_row

		# add new_row to new datagrame
print new_df






	
#print cofin_grants_loan_data_short




