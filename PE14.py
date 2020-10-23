# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:46:19 2018

@author: jakob
"""
import time

t = time.time()

def odd(n):
    return 3*n + 1

def even(n):
    return n/2

def collatz(n,l):
        if(int(n)==1 or l > 99999999999):
            return l
        if n%2 == 0:
            n = even(n)
        else:
            n = odd(n)
        l+=1
        return collatz(n,l)
        

lon = 0
longest = 0
for i in range(1000000):
    ans = collatz(i+1,0)
    if ans > lon:
        lon = ans
        longest = i+1

dt = time.time()-t
print("Best starting number is " + str(longest) + " with a length of " + str(lon) + "!")
print("That took: " + str(dt) + " seconds!")
#You have been Schauser-corrupted!!