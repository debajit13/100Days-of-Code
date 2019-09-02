# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:58:47 2019

@author: Debajit
"""

import time
import os
import pandas

while True:
    if os.path.exists("temps-today.csv"):
        data = pandas.read_csv("temps-today.csv")
        #print(data)
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10)   
    
