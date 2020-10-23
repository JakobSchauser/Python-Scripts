#pyclock
import datetime
import math

pi = str(math.pi)
cDT = datetime.datetime.now()
h = str(cDT.hour)
m = str(cDT.minute)

t_s = str(h+m)

for d in pi:
    if(t_s[0] == str(d)):
        print(d)