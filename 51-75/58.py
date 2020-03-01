from common import is_prime

def get_percent(n):
    count = 1
    prime_count = 0
    plus = 2
    current = 1
    i = 0
    while prime_count/count > .1 or plus < n:
        i = 0
        while i < 4:
            current += plus
            count += 1
            if(is_prime(current)):
                prime_count += 1
            i += 1
        plus += 2
        print(prime_count/count)
        print(plus)
    return prime_count/count

print(get_percent(7))
