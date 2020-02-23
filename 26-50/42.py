triangles = []

for n in range(1,20):
    triangles.append(int(n*(n+1)/2))

with open('26-50/42.txt') as f:
    lines = [line.rstrip() for line in f]

words = []
temp = lines[0].split(',')
for x in temp:
    y = x.replace('"', '')
    words.append(y)

total = 0

for x in words:
    count = 0
    for i in x.lower():
        count += ord(i)-96
    if count in triangles:
        total += 1

print(total)