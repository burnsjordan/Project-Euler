import math

def is_prime(n):
    if(n == 1 or n == 0):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    else:
        return True

def is_palindrome(n):
    s = str(n)
    for i in range(0, int(len(s)/2)):
        if(not s[i] == s[len(s)-1-i]):
            return False
    return True