import math

def is_pent(r):
    n = (math.sqrt(24*r+1)+1)/6
    if(n % 1 == 0 and n > 0):
        return True
    else:
        return False

def is_hex(r):
    n = (math.sqrt(8*r+1)+1)/4
    if(n % 1 == 0 and n > 0):
        return True
    else:
        return False

for i in range(1,10000000000):
    if(is_pent(i) and is_hex(i)):
        print(i)
