import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    else:
        return True

def is_circ(n):
    if(not is_prime(n)):
        return False
    l = []
    for i in str(n):
        l.append(i)
    acp = True
    for j in range(0,len(l)):
        cp = ''
        for k in range(0, len(l)):
            cp += l[k-j]
        if(not is_prime(int(cp))):
            acp = False
    return acp

count = 0

for i in range(2, 1000000):
    if(is_circ(i)):
        count += 1

print(count)
