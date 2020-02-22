digits = ['1','2','3','4','5','6','7','8','9']

def is_pan(f,s):
    global digits
    nums = str(f)+str(s)+str(f*s)
    if(len(nums) != 9):
        return False
    pan = True
    for i in digits:
        if(not nums.__contains__(i)):
            pan = False
    return pan

l = []

for i in range(1,10000):
    for j in range(1,int(10000/i)):
        if(is_pan(i,j)):
            l.append(i*j)

s = set(l)

total = 0
for i in s:
    total += i

print(total)