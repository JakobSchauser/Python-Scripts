# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:05:10 2018

@author: jakob
"""

import math

y_holes = []
for i in range(31):
    y_holes.append(i/10)


for i in range(10):

ls = []
for i in range(len(y_holes)):
    l1 = math.sqrt(4**2+y_holes[i]**2)
    l2 = math.sqrt(4**2+(3-y_holes[i])**2)
    
    ls. append(l1+l2*1.3)
    h1 = math.asin(y_holes[i]/l1)
    h2 = math.asin((3-y_holes[i])/)


print("The shortest path is " + str(min(ls)) + " at hole number " + str(ls.index(min(ls)))+"!")


print("The hældning for the first is: " + str() + " and the second is " str() + ".")
print()



#You have been Schauser-corrupted!!