import math

nums = []

for a in set(range(10)):
    for b in (set(range(10))-set([a])):
        for c in (set(range(10))-set([a])-set([b])):
            for d in (set(range(10))-set([a])-set([b])-set([c])):
                for e in (set(range(10))-set([a])-set([b])-set([c])-set([d])):
                    for f in (set(range(10))-set([a])-set([b])-set([c])-set([d])-set([e])):
                        for g in (set(range(10))-set([a])-set([b])-set([c])-set([d])-set([e])-set([f])):
                            for h in (set(range(10))-set([a])-set([b])-set([c])-set([d])-set([e])-set([f])-set([g])):
                                for i in (set(range(10))-set([a])-set([b])-set([c])-set([d])-set([e])-set([f])-set([g])-set([h])):
                                    for j in (set(range(10))-set([a])-set([b])-set([c])-set([d])-set([e])-set([f])-set([g])-set([h])-set([i])):
                                        nums.append(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j))

print(nums[999999])

# num = 1000000
# print(num - math.factorial(9)*2) ### 2
# num -= math.factorial(9)*2
# print(num - math.factorial(8)*6) ### 7
# num -= math.factorial(8)*6
# print(num - math.factorial(7)*6) ### 8
# num -= math.factorial(7)*6
# print(num - math.factorial(6)*2) ### 3
# num -= math.factorial(6)*2
# print(num - math.factorial(5)*5) ### 9
# num -= math.factorial(5)*5
# # print(num - math.factorial(4)*1) ### 1
# num -= math.factorial(4)*1
# # print(num - math.factorial(3)*2) ### 4
# num -= math.factorial(3)*2
# # print(num - math.factorial(2)*2) ### 5
# num -= math.factorial(2)*2
# print(num - math.factorial(1)*0) ### 0
# ### 6
# # 2783914506

# available = set(range(10))

# def get_perm(n, f, a):
#     global available
#     if(f == 0):
#         return str(list(available)[0])
#     perm = ''
#     i = 1
#     not_found = True
#     while(i <= f and not_found):
#         if(n <= math.factorial(f)*i):
#             perm += str(list(a)[i-1])
#             temp = [int(perm)]
#             not_found = False
#             a = a - set(temp)
#             break
#         i += 1
#     perm += get_perm(n - math.factorial(f)*(i-1), f-1, a)
#     return perm


# print(get_perm(1000000, 9, available))