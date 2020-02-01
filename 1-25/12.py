import math

triangle = 1
increment = 2
count = 0
current = 10

def count_divisors(n):
    divisors = 0
    for i in range(int(math.sqrt(n))):
        if(n % (i+1) == 0):
            if((i+1)**2 == n):
                divisors += 1
            else:
                divisors += 2
    return divisors

while (count_divisors(triangle) < 500):
    if (count_divisors(triangle) > count):
        print(count)
        count = count + 10
    triangle = triangle + increment
    increment += 1

print(triangle)