digits = ['1','2','3','4','5','6','7','8','9']

def is_pan(n):
    global digits
    nums = str(n)
    if(len(nums) != 9):
        return False
    pan = True
    for i in digits:
        if(not nums.__contains__(i)):
            pan = False
    return pan

m = 0

for i in range(1,10000):
    for j in range(2, 10):
        s = ''
        for k in range(1,j+1):
            s += str(i*k)
        if(is_pan(int(s))):
            if(int(s) > m):
                m = int(s)

print(m)
