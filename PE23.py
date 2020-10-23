# -*- coding: utf-8 -*-
import math

top = 28123
abundant = []


for i in range(11,top):
        sums = 0
        for j in range(1,math.ceil(i/2)+1):
            if i%j == 0:
                sums += j
        if(sums > i):
            abundant.append(i)
#print(abundant)

twoA = []

for a in abundant:
    for b in abundant:
        if a+b <= top:
            twoA.append(a+b)


tSum = sum(set(twoA))       
allnums = (top**2+top)/2

print(abundant)

print(allnums-tSum)
#You have been Schauser-corrupted!!