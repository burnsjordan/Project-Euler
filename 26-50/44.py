import math

pents = []
p_count = 10000
width = 10000
for i in range(1,p_count):
    pents.append(int(i*(3*i-1)/2))

m = 100000000000

def is_pent(r):
    n = (math.sqrt(24*r+1)+1)/6
    if(n % 1 == 0 and n > 0):
        return True
    else:
        return False

for i in range(len(pents)):
    for j in range(max(i-width,1),min(i+width,len(pents))):
        if(is_pent(abs(pents[i]-pents[j])) and is_pent(pents[i]+pents[j])):
            if(m > abs(pents[i]-pents[j])):
                m = abs(pents[i]-pents[j])

print(m)