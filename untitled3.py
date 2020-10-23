import matplotlib.pyplot as plt
import math
import time
import sympy 
 
x_range = 1000
def fact(a):
    prod = 1
    for i in range(2,a):
        prod *= i
    return prod

def betterfact(a):
    summ = 10**sum([math.log(_) for _ in range(2,a)])
    return summ


#x = [_ for _ in range(int(x_range))]
#y = [choose(len(x),_) for _ in x]

t1 = time.time()
for i in range(x_range):
    fact(x_range)
print("normal took " + str(time.time() - t1))
t2 = time.time()
for i in range(x_range):
    math.factorial(x_range)
print("'better' factorial took " + str(time.time() - t2))
