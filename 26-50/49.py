import math
from itertools import permutations

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    else:
        return True

def prop_one(a,b,c):
    if(not is_prime(a)):
        return False
    if(not is_prime(b)):
        return False
    if(not is_prime(c)):
        return False
    return True

def prop_two(a,b,c):
    p = list(map("".join, permutations(str(a))))
    if(not p.__contains__(str(b))):
        return False
    if(not p.__contains__(str(c))):
        return False
    return True

for i in range(1000,10000):
    for j in range(1,5000):
        if(i+2*j<10000 and i+j<10000 and prop_one(i,i+j,i+2*j) and prop_two(i,i+j,i+2*j)):
            print(str(i)+str(i+j)+str(i+2*j))