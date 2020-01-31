current = 1
best = 0
mod = 100000
best_index = 1

def get_chain_length(n):
    count = 1
    while(n > 1):
        if(n % 2 == 0):
            n = n / 2
        else:
            n = 3*n + 1
        count = count + 1
    return count

while current < 1000000:
    if(current > mod):
        print(mod)
        mod = mod + 100000
    temp = get_chain_length(current)
    if(temp > best):
        best = temp
        best_index = current
    current = current + 1

print(best)
print(best_index)