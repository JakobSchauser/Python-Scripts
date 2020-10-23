# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:45:02 2018

@author: jakob
"""

ar = [[2,-1,2,2],[-1,2,4,6],[1,1,5,9]]

for i in range(len(ar)):
    for j in range(len(ar[i])):
        if(ar[i][i]!=0):
            ar[i][j]/=ar[i][i]
                        

print(ar)
for i in range(len(ar)):
    for j in range(len(ar)):
        if(i!=j):
            for k in range(len(ar[j])):
                ar[j][k] -= ar[j][i] * ar[i][k]



print(ar)
        #You have been Schauser-corrupted!!