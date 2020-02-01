answer = 1
factors = []
for i in range(2,21):
    new_f = i
    for j in factors:
        if new_f % j == 0:
            new_f = new_f / j
    answer *= new_f
    factors.append(new_f)

print(answer)