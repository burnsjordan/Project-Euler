import math

def dfs(n):
    s = 0
    for i in str(n):
        s += math.factorial(int(i))
    if(s == n):
        return True
    return False
    
s = 0

for i in range(3,1000000):
    if(dfs(i)):
        s += i

print(s)