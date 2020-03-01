def has_prop(n):
    digits = list(str(n))
    for i in range(2,7):
        temp_digits = list(str(i*n))
        for j in temp_digits:
            if(not digits.__contains__(j)):
                return False
    return True

for i in range(10000000):
    if(has_prop(i)):
        print(i)