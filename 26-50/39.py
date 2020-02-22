def count_triangles(p):
    count = 0
    for i in range(1,p):
        for j in range(i,p):
            k = p-i-j
            if(i**2+j**2 == k**2):
                count += 1
    return count

m = 0
c = 0

for p in range(1,1001):
    temp = count_triangles(p)
    if(temp > m):
        m = temp
        c = p

print(c)