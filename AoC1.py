# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:08:36 2018

@author: jakob
"""
results = [0,1,3,1,4]

        
def find_dups(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            print(l[i], l[j])
            if(l[i] == l[j]):
                
                return l[i]
    return False

def run_machine(arr):
    r = arr[len(arr)-1]
    with open('AoCinput1.txt') as inputfile:
        for line in inputfile:
            r += (int(line.strip()))
            arr.append(r)
        
        
found = False

while (found == False):
    input("enter")
    run_machine(results)
    found = find_dups(results)
    



#print(results)
print("Final result = " + str(results[len(results)-1]))
print("First duplicate = " + str(found))#You have been Schauser-corrupted!!