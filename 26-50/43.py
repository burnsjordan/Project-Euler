digits = []
for i in range(0,10):
    digits.append(str(i))

def is_pan(n):
    nums = str(n)
    for i in digits:
        if(not nums.__contains__(i)):
            return False
    return True

def has_prop(n):
    s = str('{:010}'.format(n))
    if(int(s[7]+s[8]+s[9]) % 17 != 0):
        return False
    if(int(s[6]+s[7]+s[8]) % 13 != 0):
        return False
    if(int(s[5]+s[6]+s[7]) % 11 != 0):
        return False
    if(int(s[4]+s[5]+s[6]) % 7 != 0):
        return False
    if(int(s[3]+s[4]+s[5]) % 5 != 0):
        return False
    if(int(s[2]+s[3]+s[4]) % 3 != 0):
        return False
    if(int(s[1]+s[2]+s[3]) % 2 != 0):
        return False
    return True


# Generate 5 digit numbers whose 3 digit components are divisible by 17, 13, and 11

l_17 = []
l_13 = []
l_11 = []
intersect_1 = []
intersect = []
for i in range(1,1000):
    if(i % 17 == 0):
        if(i < 100):
            l_17.append('0' + str(i))
        else:
            l_17.append(str(i))
    if(i % 13 == 0):
        if(i < 100):
            l_13.append('0' + str(i))
        else:
            l_13.append(str(i))
    if(i % 11 == 0):
        if(i < 100):
            l_11.append('0' + str(i))
        else:
            l_11.append(str(i))

for i in l_17:
    for j in l_13:
        if(j.endswith(i[:2])):
            intersect_1.append(j+i[-1])

for i in intersect_1:
    for j in l_11:
        if(j.endswith(i[:2])):
            intersect.append(j+i[-2:])

total = 0

for i in range(100000):
    for j in intersect:
        if(has_prop(int(str(i)+j)) and is_pan(int(str(i)+j))):
            total += int(str(i)+j)
    
print(total)