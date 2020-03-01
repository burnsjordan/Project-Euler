from common import is_prime

prime_list = []

for i in range(10000):
    if(is_prime(i)):
        prime_list.append(i)

def has_prop1(a, b):
    if(not is_prime(int(str(a)+str(b)))):
        return False
    elif(not is_prime(int(str(b)+str(a)))):
        return False
    else:
        return True

def has_prop2(a, b, c):
    if(not is_prime(int(str(a)+str(b)))):
        return False
    elif(not is_prime(int(str(b)+str(a)))):
        return False
    elif(not is_prime(int(str(a)+str(c)))):
        return False
    elif(not is_prime(int(str(c)+str(a)))):
        return False
    elif(not is_prime(int(str(b)+str(c)))):
        return False
    elif(not is_prime(int(str(c)+str(b)))):
        return False
    else:
        return True

def has_prop3(a, b, c, d):
    if(not is_prime(int(str(a)+str(b)))):
        return False
    elif(not is_prime(int(str(b)+str(a)))):
        return False
    elif(not is_prime(int(str(a)+str(c)))):
        return False
    elif(not is_prime(int(str(c)+str(a)))):
        return False
    elif(not is_prime(int(str(a)+str(d)))):
        return False
    elif(not is_prime(int(str(d)+str(a)))):
        return False
    elif(not is_prime(int(str(b)+str(c)))):
        return False
    elif(not is_prime(int(str(c)+str(b)))):
        return False
    elif(not is_prime(int(str(b)+str(d)))):
        return False
    elif(not is_prime(int(str(d)+str(b)))):
        return False
    elif(not is_prime(int(str(c)+str(d)))):
        return False
    elif(not is_prime(int(str(d)+str(c)))):
        return False
    else:
        return True

def has_prop(a, b, c, d, e):
    if(not is_prime(int(str(a)+str(b)))):
        return False
    elif(not is_prime(int(str(b)+str(a)))):
        return False
    elif(not is_prime(int(str(a)+str(c)))):
        return False
    elif(not is_prime(int(str(c)+str(a)))):
        return False
    elif(not is_prime(int(str(a)+str(d)))):
        return False
    elif(not is_prime(int(str(d)+str(a)))):
        return False
    elif(not is_prime(int(str(a)+str(e)))):
        return False
    elif(not is_prime(int(str(e)+str(a)))):
        return False
    elif(not is_prime(int(str(b)+str(c)))):
        return False
    elif(not is_prime(int(str(c)+str(b)))):
        return False
    elif(not is_prime(int(str(b)+str(d)))):
        return False
    elif(not is_prime(int(str(d)+str(b)))):
        return False
    elif(not is_prime(int(str(b)+str(e)))):
        return False
    elif(not is_prime(int(str(e)+str(b)))):
        return False
    elif(not is_prime(int(str(c)+str(d)))):
        return False
    elif(not is_prime(int(str(d)+str(c)))):
        return False
    elif(not is_prime(int(str(c)+str(e)))):
        return False
    elif(not is_prime(int(str(e)+str(c)))):
        return False
    elif(not is_prime(int(str(d)+str(e)))):
        return False
    elif(not is_prime(int(str(e)+str(d)))):
        return False
    else:
        return True

# for i in prime_list:
#     if(has_prop(3,7,109,673,i)):
#         print(792+i)

for i in range(len(prime_list)):
    print(i)
    for j in range(i+1, len(prime_list)):
        if(has_prop1(prime_list[i], prime_list[j])):
            for k in range(j+1, len(prime_list)):
                if(has_prop2(prime_list[i], prime_list[j], prime_list[k])):
                    for l in range(k+1, len(prime_list)):
                        if(has_prop3(prime_list[i], prime_list[j], prime_list[k], prime_list[l])):
                            for m in range(l+1, len(prime_list)):
                                if(has_prop(prime_list[i],prime_list[j],prime_list[k],prime_list[l],prime_list[m])):
                                    print('')
                                    print(prime_list[i]+prime_list[j]+prime_list[k]+prime_list[l]+prime_list[m])
                                    print('')

# for i in range(len(prime_list)):
#     print(i)
#     for j in range(i+1, len(prime_list)):
#         for k in range(j+1, len(prime_list)):
#             for l in range(k+1, len(prime_list)):
#                 for m in range(l+1, len(prime_list)):
#                     if(has_prop(prime_list[i],prime_list[j],prime_list[k],prime_list[l],prime_list[m])):
#                         print('')
#                         print(prime_list[i]+prime_list[j]+prime_list[k]+prime_list[l]+prime_list[m])
#                         print('')