l = 0
i = 1
d = ''
while l < 1000000:
    l += len(str(i))
    d += str(i)
    i += 1
print(int(d[0])*int(d[9])*int(d[99])*int(d[999])*int(d[9999])*int(d[99999])*int(d[999999]))