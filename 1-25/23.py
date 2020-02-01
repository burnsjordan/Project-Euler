def is_abundant(n):
    divisor_sum = 0
    for i in range(1,n):
        if(n % i == 0):
            divisor_sum += i
    if(divisor_sum > n):
        return True
    else:
        return False

abundants = []
sums = []
possibles = []
total = 0

for i in range(1,28123):
    if(is_abundant(i)):
        abundants.append(i)
    possibles.append(i)

for j in range(len(abundants)):
        for k in range(len(abundants)):
            sums.append(abundants[j]+abundants[k])

nots = list(set(possibles) - set(sums))

for i in nots:
    total += i

print(total)