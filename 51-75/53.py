from math import factorial

def choose(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

count = 0
for i in range(1,101):
    for j in range(i):
        if(choose(i, j) > 1000000):
            count += 1
print(count)