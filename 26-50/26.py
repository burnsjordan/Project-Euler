from decimal import Decimal, getcontext

getcontext().prec = 10000

def only_zeros(x):
    only_zeros = True
    for i in x:
        if(int(i) != 0):
            only_zeros = False
    return only_zeros

def find_cycle(x):
    if(len(x) <= 1):
        return 0
    lead = x[0]
    i = 1
    while i < len(x):
        if(x[i] == lead):

            if(x[0:i] == x[i:2*i] and not only_zeros(x[0:i]) and x[0:i] == x[2*i:3*i] and x[0:i] == x[3*i:4*i]):
                # print(x[0:i])
                return(i)
        i += 1
    return find_cycle(x[1:])

best = 0

for i in range(1,1000):
    # print(Decimal(1) / Decimal(i))
    if(find_cycle(str(Decimal(1) / Decimal(i))[2:]) > best):
        best = i

print(best)