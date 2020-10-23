# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 08:59:38 2018

@author: jakob
"""

threes = 0
twos = 0

def find_dups(l):
    global threes
    global twos
    d2 = False
    d3 = False
    for i in range(len(l)):
        count = 1
        for j in range(len(l)):
            if(j != i):
                #input(str(l[i]) +" "+ str( l[j]) + " count = " + str(count))
                #print("2s: " + str(twos) + " 3s: "+ str(threes))
                if(l[i] == l[j]):
                    count += 1
        if(count == 2 and not d2):
            twos += 1
            d2 = True
        if(count == 3 and not d3):
            threes += 1
            d3 = True
    return False



with open('AoCinput2.txt') as inputfile:
    for line in inputfile:
        l = (line.strip())
        find_dups(l)
            
print("Checksum = ", threes*twos)


#part 2:

def find_common(l1,l2):
    common = []
    for i in range(len(l1)):
        if(l1[i] == l2[i]):
            common.append(l1[i])
    return common

inputs = []
with open('AoCinput2.txt') as inputfile:
    for line in inputfile:
        inputs.append(line.strip())
        

for i in range(len(inputs)):
    for j in range(i,len(inputs)):
        l1 = inputs[i].strip()
        l2 = inputs[j].strip()
        c = find_common(l1,l2)
        if(len(c) == len(inputs[i])-1):
            print(c)
        #You have been Schauser-corrupted!!