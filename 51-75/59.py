from operator import xor

with open('51-75/59.txt') as f:
    lines = [line.rstrip() for line in f]
temp = lines[0].split(',')

def decrypt(enc, text):
    d = []
    dn = []
    mod = len(enc)
    for i in range(len(text)):
        temp = xor(int(text[i]),enc[i%mod])
        if(temp > 31 and temp < 123):
            d.append(chr(temp))
            dn.append(temp)
        else:
            return False
    print("".join(d))
    print(sum(dn))
    return True

for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            decrypt([i,j,k],temp)