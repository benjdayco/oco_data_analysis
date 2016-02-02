import pandas as pd
import numpy as np

all_psc_data = pd.read_csv("data_files/all_psc.csv")
cofin_grants_loan_data = pd.read_csv("data_files/cofin_grants_loans.csv")

all_psc_data = all_psc_data.astype(str)

psc_convert = all_psc_data.copy()

psc_convert['approval number'] = all_psc_data['approval number'].apply(lambda x: x.zfill(4))

psc_convert['approval number'] = all_psc_data['approval number'].apply(lambda x: x.zfill(4))

psc_convert.to_csv("data_files/psc_convert.csv")

print psc_convert['approval number']