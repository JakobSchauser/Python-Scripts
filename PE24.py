import time
import numpy as np

t_s = time.time

start = [0,1,2,3,4,5,6,7,8,9]
highs = []

p = 1

def change(n,p):
    if n < 0:
        n = 9
        p += 1
    if(p == 9):
        return
    perm = start.copy()
    perm[n], perm[n-p] = perm[n-p], perm[n]
    print(perm)
    change(n-1,p)
    

change(9,p)


#print(len(highs))#You have been Schauser-corrupted!!