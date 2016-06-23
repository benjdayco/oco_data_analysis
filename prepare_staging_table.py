#
# Script for converting raw dump files from CoFin to a staging table file for importing to CoMs
#

import pandas as pd
import numpy as np

#read data files: raw dump that includes product approval number
#
cofin_grant_loans_all_raw = pd.read_csv("data_files/cofin_grants_loans_raw_ 6-22-2016.csv")

#remove records with all blank columns (noise from lotus notes)
cofin_grant_loans_all = cofin_grant_loans_all_raw.dropna(subset = ['Loan/Grant Title'] , how='all')

#cofin_grant_loans_all
cofin_grant_loans_all.info()

print cofin_grant_loans_all

cofin_grant_loans_all['Anchor Product'] = ''

print "processing..."

#extract acnchor product
for index,row in cofin_grant_loans_all.iterrows():
    #temporary store approval number of current row
    approval_number_orig = str(row['Approval Numbers'])

    #split approval number into array by character
    approval_number_split =  approval_number_orig.split("/")
    cofin_grant_loans_all['Anchor Product'][index] = str(approval_number_split[0])

cofin_grant_loans_all.to_csv("data_files/cofin_grants_loans_dump_with_anchor_6-22-2016.csv")

print "Done!"
