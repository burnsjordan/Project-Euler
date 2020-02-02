count = 1
plus = 2
current = 1
i = 0
while plus < 1001:
    i = 0
    while i < 4:
        current += plus
        count += current
        i += 1
    plus += 2

print(count)