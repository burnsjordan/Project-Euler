f1 = 1
f2 = 1
index = 2

while (len(str(f2)) < 1000):
    temp = int(f1+f2)
    f1 = int(f2)
    f2 = int(temp)
    index += 1

print(f2)
print(index)