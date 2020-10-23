import random

primelist = []
croaklist =  [True,True,True,True,False,False,True,True,True,False,True,True,False,True,False]

def find_primes(num):
    ps = []
    
    for i in range(2,num):
        isprime = True
        for ii in range(2,i):
            if(i%ii==0):
                isprime = False
                break
        if(isprime):
            ps.append(i)
    return ps


def croak(n):
    if n in primelist:
        if(random.choice([0,1,2])>0):
            return True
        else:
            return False
    else:
        if(random.choice([0,1,2])>1):
            return True
        else:
            return False

def let_frog_loose():
    place = random.randint(1,500)
    for cl in croaklist:
        c = croak(place)
        if(c!=cl):
            return False
        place += random.choice([-1,1])
        if(place > 500):
            place = 499
        elif(place < 1):
            place = 2
    return True

primelist = find_primes(500)

num_runs = 5*10**8
num_true = 0


for i in range(num_runs):
    l = let_frog_loose()
    if(l):
        num_true += 1
        print(i/num_runs*100)
    

print(num_true, num_runs)
print(num_runs/num_true)