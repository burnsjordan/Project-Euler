import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    else:
        return True

def is_pan(n,d):
    digits = []
    for i in range(1,d+1):
        digits.append(str(i))
    nums = str(n)
    if(len(nums) != d):
        return False
    pan = True
    for i in digits:
        if(not nums.__contains__(i)):
            pan = False
    return pan

m = 0

p_list = []

i = 3

while i < 10000000:
    if(is_prime(i)):
        p_list.append(i)
    i += 2

for i in p_list:
    for j in range(4,10):
        if(is_pan(i,j)):
            if(i > m):
                m = i

print(m)
