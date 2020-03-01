import common as c
from copy import deepcopy

def replace_one(n):
    s = list(str(n))
    M = 0
    for i in range(len(s)):
        count = 0
        if(i == 0):
            t = 1
        else:
            t = 0
        for j in range(t,10):
            temp = deepcopy(s)
            temp.insert(i, str(j))
            if(c.is_prime(int("".join(temp)))):
                count += 1
        if(count > M):
            M = count
    return M

def replace_two(n):
    s = list(str(n))
    M = 0
    for i in range(len(s)):
        for k in range(i, len(s)+1):
            count = 0
            if(i == 0):
                t = 1
            else:
                t = 0
            for j in range(t,10):
                temp = deepcopy(s)
                temp.insert(i, str(j))
                temp.insert(k, str(j))
                if(c.is_prime(int("".join(temp)))):
                    count += 1
            if(count > M):
                M = count
    return M

def replace_three(n):
    s = list(str(n))
    M = 0
    for i in range(len(s)):
        for k in range(i, len(s)+1):
            for l in range(k, len(s)+2):
                count = 0
                if(i == 0):
                    t = 1
                else:
                    t = 0
                for j in range(t,10):
                    temp = deepcopy(s)
                    temp.insert(i, str(j))
                    temp.insert(k, str(j))
                    temp.insert(l, str(j))
                    if(c.is_prime(int("".join(temp)))):
                        count += 1
                if(count > M):
                    M = count
    return M

replace_three(233)

for i in range(10000):
    if(replace_one(i) == 8):
        print(i)
    if(replace_two(i) == 8):
        print(i)
    if(replace_three(i) == 8):
        print(i)