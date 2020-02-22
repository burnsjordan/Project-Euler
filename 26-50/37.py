import math

def is_prime(n):
    if(n == 1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    else:
        return True

total = 0

for i in range(10, 1000000):
    s = str(i)
    yes = True
    for j in range(len(s)):
        if(not (is_prime(int(s[j:])) and is_prime(int(s[:len(s)-j])))):
            yes = False
    if(yes):
        total += i

print(total)