fib1 = 1
fib2 = 2
sum = 0

while (fib2 <= 4000000):
    temp = fib1 + fib2
    sum += fib2
    fib1 = fib2
    fib2 = temp
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp
    temp = fib1 + fib2

print(sum)