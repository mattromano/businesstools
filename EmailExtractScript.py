# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:01:37 2019

@author: mattr
"""

import pandas as pd
import numpy as np

path = input('What is the path of the export CSV?')
personname = input('Export name?')

sent =  pd.read_csv(path)

extsent = pd.DataFrame(sent[sent['To: (Type)'].str.contains('SMTP',na=False)])

toemail = pd.DataFrame(sent[sent.columns[[5,6]]])

toemail = toemail[toemail['To: (Address)'].str.contains('@',na=False)]

toemail['To: (Address)'] = toemail['To: (Address)'].str.split(';')
toemail['To: (Name)'] = toemail['To: (Name)'].str.split(';')

email_list = []
for address in toemail['To: (Address)']:
    for a in address:
        email_list.append(a)

name_list = []
for address in toemail['To: (Name)']:
    for a in address:
        name_list.append(a)

tonamlen = len(name_list)
toemaillen = len(email_list)

print('Total of %d names extracted and total of %d emails extracted'%(tonamlen,toemaillen))

new_df = pd.DataFrame()
new_df['names'] = name_list
new_df['addresses'] = email_list

df2 = new_df[~new_df['addresses'].str.contains('/o=ExchangeLabs/ou=Exchange Administrative',na=False)]

df2.to_csv('%s_to_email extract.csv' % personname)

ccsent = pd.DataFrame(sent[sent['CC: (Type)'].str.contains('SMTP',na=False)])

ccemail = pd.DataFrame(ccsent[ccsent.columns[[8,9]]])

ccemail['CC: (Address)'] = ccemail['CC: (Address)'].str.split(';')
ccemail['CC: (Name)'] = ccemail['CC: (Name)'].str.split(';')

cc_email_list = []
for address in ccemail['CC: (Address)']:
    for a in address:
        cc_email_list.append(a)
        
cc_name_list = []
for name in ccemail['CC: (Name)']:
    for a in name:
        cc_name_list.append(a)
        
ccnamlen = len(cc_name_list)
ccemaillen = len(cc_email_list)

print('Total of %d names extracted and total of %d emails extracted from CCs'%(ccnamlen,ccemaillen))

cc_df = pd.DataFrame()
cc_df['Names'] = cc_name_list
cc_df['Addresses'] = cc_email_list

cc_df = cc_df[~cc_df['Addresses'].str.contains('/o=ExchangeLabs/ou=Exchange Administrative',na=False)]

cc_df.to_csv('%s_cc_email_extract.csv' % personname)