import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    else:
        return True

primes = []

for i in range(2,1000000):
    if(is_prime(i)):
        primes.append(i)

i = 600
not_done = True
while i > 90 and not_done:
    print(i)
    for j in range(len(primes)-i,0,-1):
        s = sum(primes[j:j+i])
        if(primes.__contains__(s) and not_done):
            print(s)
            not_done = False
    i -= 1