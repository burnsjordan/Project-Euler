import common as c

def is_lychrel(n, j):
    t = []
    for i in range(len(list(str(n)))-1, -1, -1):
        t.append(list(str(n))[i])
    t = int("".join(t))
    if(c.is_palindrome(n+t)):
        return False
    elif(j == 0):
        return True
    else:
        return is_lychrel(n+t, j-1)

count = 0
for i in range(1,10000):
    if(is_lychrel(i, 50)):
        count += 1
print(count)