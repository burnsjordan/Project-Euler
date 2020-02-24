import math

def is_prime(n):
    if(n == 1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    else:
        return True

def get_factors(n):
    factors = []
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            factors.append(i)
            factors.append(int(n/i))
    return factors

def get_prime_factors(n):
    factors = []
    for i in get_factors(n):
        if(is_prime(i)):
            factors.append(i)
        else:
            temp = get_prime_factors(i)
            for j in temp:
                factors.append(j)
    return set(factors)

def count_distinct_factors(n):
    return len(get_prime_factors(n))

not_done = True
i = 1
while i < 1000000 and not_done:
    if(count_distinct_factors(i) == 4 and count_distinct_factors(i+1) == 4 and count_distinct_factors(i+2) == 4 and count_distinct_factors(i+3) == 4):
        print(i)
        not_done = False
    i += 1
