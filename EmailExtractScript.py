# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:01:37 2019

@author: mattr
"""

import pandas as pd
import numpy as np

sent =  pd.read_csv('LindseySent.csv')

extsent = pd.DataFrame(sent[sent['To: (Type)'].str.contains('SMTP',na=False)])

toemail = pd.DataFrame(sent[sent.columns[[5,6]]])

toemail = toemail[toemail['To: (Address)'].str.contains('@',na=False)]

toemail['To: (Address)'] = toemail['To: (Address)'].str.split(';')
toemail['To: (Name)'] = toemail['To: (Name)'].str.split(';')

email_list = []
for address in toemail['To: (Address)']:
    for a in address:
        email_list.append(a)

toemail.to_csv('PorterToAddress.csv')

cc_contacts_count = len(email_list)

print()