i = 999
answer = 0
while i > 99:
    j = 999
    while j > 99:
        product = i*j
        prod_str = str(i*j)
        if prod_str == prod_str[::-1]:
            if product > answer:
                answer = product
        j -= 1
    i -= 1

print(answer)