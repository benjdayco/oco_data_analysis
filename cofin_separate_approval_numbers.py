import pandas as pd
import numpy as np

# Set some pandas options for controlling output display
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

#read data file
cofin_grants_loan_data_raw = pd.read_csv("data_files/loan_grants_test.csv")

#remove records with all blank columns (noise from lotus notes)
cofin_grants_loan_data = cofin_grants_loan_data_raw.dropna(subset = ['Approval Numbers','Proj No'] , how='all')


#create dataframe with only Partner, Approval Numbers, Proj. No, and Loan/Grant Title column"
cofin_grants_loan_data_short = cofin_grants_loan_data[['Partner', 'Approval Numbers', 'Proj No', 'Loan/Grant Title']]
	
#iterate each row
for index,row in cofin_grants_loan_data_short.iterrows():

	print row['Proj No']

	#temporary store approval number of current row
	approval_number_orig = str(row['Approval Numbers'])

	#split approval number into array by character
	approval_number_split =  approval_number_orig.split("/")
	
	#itererate through each approval number in array
	for number in approval_number_split:
		print number
 
	#insert current approval number into new dataframe with row[Project No]
	new_row = row
	new_row
	print new_row
	#insert row as series
	# add number to series




	
#print cofin_grants_loan_data_short




