# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:44:00 2018

@author: jakob
"""
import math


inputtxt = []
with open("easy50.txt") as inputfile:
    for line in inputfile:
        inputtxt.append(line[:])
num = 2
sol = [[[___ for ___ in range(10)] for __ in range(9)] for _ in range(9)]
sud = [[int(inputtxt[num][i*9+ii]) for ii in range(9)] for i in range(9)]


def column(a,x):
    return [r[x] for r in a]

def square(a,x,y):
    sqr = []
    for i in range(3):
        for ii in range(3):
            sqr.append(a[math.floor(y/3)*3+i][math.floor(x/3)*3+ii])
    return sqr


def solve():
    for x in range(9):
        for y in range(9):
            if(sud[y][x]==0):
                c = column(sud,x)
                r = sud[y]
                sqr = square(sud,x,y)
                #print(sud[y][x])
                used = list(set(c+r+sqr))
                #print(used)
                #print(used)
                for s in sol[y][x]:
                    if s in used:
                        sol[y][x].remove(s)
                if(len(sol[y][x])==1):
                    print(sol[y][x])
                    sud[y][x]=sol[y][x][0]
            
        
        
        
#You have been Schauser-corrupted!!