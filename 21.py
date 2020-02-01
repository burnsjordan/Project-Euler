def sum_divisors(n):
    sum = 0
    for i in range(1,n):
        if(n % i == 0):
            sum += i
    return sum

def is_amicable(n):
    d_sum = sum_divisors(n)
    d_sum2 = sum_divisors(d_sum)
    if(d_sum2 == n and d_sum != n):
        return True
    else:
        return False

sum = 0

for i in range(1, 10000):
    if(is_amicable(i)):
        sum += i

print(sum)