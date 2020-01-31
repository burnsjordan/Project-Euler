with open('13.txt') as f:
    lines = [int(line.rstrip()) for line in f]

sum = 0
for x in lines:
    sum = sum + x
print(sum)