Fredes mor
from random import choice as c

d = range(1,7)

A, B ,s, m = [1 for _ in d], [d[-1] for _ in d], 1, []

o = lambda n: (n >= 1 and n <= len(d)) 

for i in range(300):
    r = c(d)-1
    if(o(A[r]+s) and o(B[r]-s)):
        A[r] += s
        B[r] -= s
    m.append([sum(A),sum(B)])
    s *= -1
