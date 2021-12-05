# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 10:52:05 2021

@author: gabri
"""

import pandas as pd
import numpy as np

data_csv = pd.read_csv("1.csv", sep=';')
values = data_csv.values
col_names = list(data_csv.columns)

#1
even = values[::2,:]
uneven = values[1::2, :]
diff = even - uneven

#2
avg = diff.mean()
std = diff.std()
arr = (diff-avg)/std

#3
res3 = (values - values.mean(axis=0))/values.std(axis=0)
    
#4
res4 = values.mean(axis=0)/(values.std(axis=0)+np.spacing(values.std(axis=0)))
max4 = np.argmax(res4)