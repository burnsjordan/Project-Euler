import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    else:
        return True

squares = []
primes = []

for i in range(1,1000):
    squares.append(2*i**2)

for i in range(2,10000):
    if(is_prime(i)):
        primes.append(i)

def can_sum(n):
    if(not is_prime(n)):
        for s in squares:
            for p in primes:
                if(s+p == j):
                    return True
    else:
        return True
    return False

j = 9
while j < 10000:
    if(not can_sum(j)):
        print(j)
    j += 2