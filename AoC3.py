# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:18:34 2018

@author: jakob
"""
points = []
d = []
with open('AoCinput3.txt') as inputfile:
    for line in inputfile:
        l = (line.strip())
        i_at = l[l.find('@')+2]
        i_col = l[l.find(':')]
        i_x = l[l.find('x')]
        i_com = l[l.find(',')]
        
        points.append([,])
        
print(points[1])
print(d[1])

sqr = 0
for p in range(len(points)):
    for i in range(len(points)):
        break
        xx = max(0,min((points[i][0]+d[i][0])-points[p][0], (points[p][0]+d[p][0])-points[i][0]))
        yy = max(0,min((points[i][1]+d[i][1])-points[p][1], (points[p][1]+d[p][1])-points[i][1]))
        sqr += xx*yy
#You have been Schauser-corrupted!!