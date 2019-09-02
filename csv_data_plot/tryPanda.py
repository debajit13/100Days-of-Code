# -*- coding: utf-8 -*-
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
    
