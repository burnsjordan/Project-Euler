def is_pal(n):
    s = str(n)
    b = str(bin(n))[2:]
    for i in range(0, int(len(s)/2)):
        if(not s[i] == s[len(s)-1-i]):
            return False
    for j in range(0, int(len(b)/2)):
        if(not b[j] == b[len(b)-1-j]):
            return False
    return True

total = 0

for i in range(1, 1000000):
    if(is_pal(i)):
        total += i

print(total)