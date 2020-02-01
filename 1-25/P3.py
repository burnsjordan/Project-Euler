number = 600851475143
factors = []

def findFactors(n):
    i = 2
    check = True
    while i < n:
        if n % i == 0:
            factors.append(i)
            num = n / i
            findFactors(num)
            check = False
            break
        else:
            i += 1
    if check:
        factors.append(n)

findFactors(number)

print(factors.pop())