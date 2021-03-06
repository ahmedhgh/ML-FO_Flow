import os
import pandas as pd

project_path = os.path.realpath('')
headers = pd.read_excel(project_path + os.sep + 'var_names.xlsx')
# Load the data from the Excel-file with headers. Please not the project_path

#%%
# Create a list of each column, then a dictonary which is acting as the translator.
# The dictonary acts two-ways

old = headers['ORIGINAL_HEADER']
new = headers['NEW_HEADER']
d = {}
for n in range(len(old)):
    d[new[n]] = old[n]
    d[old[n]] = new[n] # So it can act two ways, bi-directional.

#%%
