# This is just 40C20
current = 0
count = 0
mod = 1000000

def is_balanced(n):
    s = str('{:040b}'.format(n))
    count = 0
    for i in s:
        if(int(i) == 1):
            count += 1
    if(count == 20):
        return True
    else:
        return False

while current < (2**40):
    if(current > mod):
        print(mod)
        mod = mod + 1000000
    if(is_balanced(current)):
        count = count + 1
    current = current + 1

print(count)