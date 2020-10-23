# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:24:34 2018

@author: jakob
"""

import csv



num = 0
with open("triangles.txt") as file:
    for r in csv.reader(file):
        row = [int(_) for _ in r]
        
        a1 = row[1]/row[0]
        a2 = row[3]/row[2]
        a3 = row[5]/row[4]
        
        b1 = -a3 < a1 and -a3 > a2
        b2 = -a3 > a1 and -a3 < a2
        if(b1 or b2):
            num+=1
            
print(num)
        

#You have been Schauser-corrupted!!