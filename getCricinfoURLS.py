# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 09:01:30 2022

@author: hgadd
"""

import os 
import regex as re
import csv
urls = []
for file in os.listdir("CountryPlayerPages"):
    print(file)
    if(".html" in file):
        with open(r"CountryPlayerPages/"+file, encoding="utf8") as f:
            text = f.read()
            text = text.split('"')
            deaths = False
            for t in text:
                urlsFound= re.findall("https://www\.espncricinfo\.com/player/.+\d+$", t)
                for url in urlsFound:
                    if(deaths and "team" not in url and url not in urls):
                        urls.append(url)
                    if("deaths" in url):
                        deaths = True
with open("CricketURLS.csv","w",  encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    for url in urls:
        writer.writerow([url])
    f.close()        