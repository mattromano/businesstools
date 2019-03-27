import pandas as pd
import numpy as np

path = input('What is the path of the contact CSV?')
listname = input('Export name?')

contactlist =  pd.read_csv(path)

inclusionlist = ['ecommerce','e-commerce','growth','marketing','creative','content','digital','social','CMO','chief marketing officer','chief strategy officer']
exclusionlist = ['intern','coordinator','assistant','jr']

df1 = pd.DataFrame(contactlist[contactlist['Title'].str.contains('|'.join(inclusionlist), case=False, na=False,)])
df2 = df1[~df1['Title'].str.contains('|'.join(exclusionlist), case=False,na=False)]

contactsfiltered = len(contactlist) - len(df2)

print('Total of %d contacts filtered' %contactsfiltered)

df2.to_csv('%s.csv' % listname)

