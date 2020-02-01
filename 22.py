with open('22.txt') as f:
    lines = [line.rstrip() for line in f]

names = []
temp = lines[0].split(',')
for x in temp:
    y = x.replace('"', '')
    names.append(y)

names.sort()

scores = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

def get_sum(s):
    sum = 0
    for i in s:
        sum += scores[i.lower()]
    return sum

total = 0

for i in range(len(names)):
    total += get_sum(names[i]*(i+1))

print(total)
