def dig_sum(n):
    s = list(str(n))
    total = 0
    for i in s:
        total += int(i)
    return total

M = 0
for i in range(100):
    for j in range(100):
        s = dig_sum(i**j)
        if(s > M):
            M = s

print(M)