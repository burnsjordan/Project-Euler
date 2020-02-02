import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))):
        if(n % i == 0):
            return False
    else:
        return True

def num_cons_primes(a, b):
    n = 0
    while(is_prime(abs(n**2+(a*n)+b))):
        n += 1
    return n

best = 0
best_a = 1
best_b = 41

for i in range(-999,1000):
    for j in range(-1000,1001):
        temp = num_cons_primes(i, j)
        if(temp > best):
            best = temp
            best_a = i
            best_b = j

print(best_a*best_b)