# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:32:13 2018

@author: jakob
"""

def binary(d):
    b = [0]
    for i in range(d):
        b[0]+=1
        if(b[0]== 2):
            for j in range(len(b)):
                if(b[j]==2):
                    b[j]=0
                    if(j+1 > len(b)-1):
                        b.append(1)
                    else:
                        b[j+1]+=1
                else:
                    break
    return "".join(str(i) for i in b)


def checkPalindrome(n):
    for i in range(int(len(n))):
        if(n[i] != n[len(n)-i-1]):
            return False
    return True
    
summ = 0
for i in range(0,10**6):
    if(checkPalindrome(str((i)))):
        if(checkPalindrome(binary(i))):
            summ += i
            print(summ)#You have been Schauser-corrupted!!