# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:10:17 2018

@author: jakob
"""
import csv
import math

rsum = []
with open("numbers.txt") as file:
    for row in csv.reader(file):
        rsum.append(math.log(int(row[0]))*int(row[1]))

print(rsum.index(max(rsum))+1)
                

#You have been Schauser-corrupted!!