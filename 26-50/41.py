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

i = 10000001

done = False

while i > 6000000:
    if(not done and is_prime(i)):
        for j in range(4,10):
            if(is_pan(i,j)):
                print(i)
                done = True
    i -= 2
