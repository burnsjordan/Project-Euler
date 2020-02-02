def is_sum_of_digits(n):
    s = 0
    for i in str(n):
        s += int(i)**5
    if(s == n):
        return True
    else:
        return False
    
total = 0

for i in range(2,5*(9**5)):
    if(is_sum_of_digits(i)):
        total += i
    
print(total)