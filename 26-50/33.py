l1 = []
l2 = []

def is_nt(x,y,z,w):
    if(z % 10 == 0 and w % 10 == 0):
        return False
    if(y == 0):
        return False
    elif(x/y >= 1):
        return False
    if(w == 0):
        return False
    elif(x/y == z/w):
        return True
    return False

for i in range(10,100):
    for j in range(10,100):
        f1 = ''
        f2 = ''
        if(i < 10):
            f1 = '0'
        if(j < 10):
            f2 = '0'
        a = f1+str(i)
        b = f2+str(j)
        if(a[0] == b[0] and a[1] != b[1]):
            if(is_nt(int(a[1]),int(b[1]),i,j)):
                l1.append(a)
                l2.append(b)
        elif(a[0] == b[1] and a[1] != b[0]):
            if(is_nt(int(a[1]),int(b[0]),i,j)):
                l1.append(a)
                l2.append(b)
        elif(a[1] == b[0] and a[0] != b[1]):
            if(is_nt(int(a[0]),int(b[1]),i,j)):
                l1.append(a)
                l2.append(b)
        elif(a[1] == b[1] and a[0] != b[0]):
            if(is_nt(int(a[0]),int(b[0]),i,j)):
                l1.append(a)
                l2.append(b)

p1 = 1
p2 = 1
for i in l1:
    p1 *= int(i)
for j in l2:
    p2 *= int(j)
    
print(p1)
print(p2)