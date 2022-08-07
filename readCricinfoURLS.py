# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 08:58:29 2022

@author: hgadd
"""

import csv
import json
import os
from cricketStatGrabber import cricketStatGrabber

playerData = []
failedURLS = []
with open('CricketURLS.csv', 'r') as f:
    reader = csv.reader(f)
    players = list(reader)
    for n in players:
        try:
            playerData.append(cricketStatGrabber(n[0]))
        except Exception as e:
            
            print(n[0])
            print(e)
            failedURLS.append(n[0])

    
# field names 
fields = ["name", "age","country", "intMatches","matches","batInns","notOuts","runs","ballsFaced","foursScored","sixesScored","catches&stumpings","bowlInns","ballsBowled","runsConceded","wickets"] 
    
# name of csv file 
filename = "playerRecords.csv"
    
# writing to csv file 

with open("FailedCricketURLS.csv","w",  encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    for url in failedURLS:
        writer.writerow([url])
    f.close()     
    
with open(filename, 'w', newline = '', encoding = 'UTF8') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
    
    # writing data rows 
    writer.writerows(playerData) 
    csvfile.close()