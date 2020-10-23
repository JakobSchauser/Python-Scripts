# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 13:45:08 2018

@author: jakob
"""
import math
from random import shuffle


times_run = 1
rounds = 500

def compare(i1,i2):
    if i1>i2:
        return 0
    if i1<i2:
        return 1
    else:
        return False
    
def krig(p1,p2):
    pile1 = []
    pile2 = []
    for i in range(3):
        pile1.append(p1.pop(i))
        pile2.append(p2.pop(i))
        
    for i in range(3):
        c = compare(pile1[0],pile2[0]) 
        if(c != False):
            return [c,pile1+pile2]
    
    
        
        
        
deck = [math.floor(_/4) for _ in range(52)]

p[][]

for t in range(times_run):
    shuffle(deck)
    p[0] = deck[:int(len(deck)/2)]
    p[1] = deck[int(len(deck)/2):]
    
    for r in range(rounds):
        c = compare(p[0][r],p2[1][r])
        if(c == False):
            krig()
        else:
            p[c].append(p[0].pop(r))
            p[c].append(p[1].pop(r))
            
    
    #You have been Schauser-corrupted!!