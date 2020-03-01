from fractions import Fraction
import sys
sys.setrecursionlimit(10000)

def frac_expansion2(j):
    if(j == 0):
        return 2
    else:
        return Fraction(2+(1/frac_expansion2(j-1)))

def frac_expansion1(j):
    return Fraction(1 + 1/frac_expansion2(j-1))

def digit_count(n):
    return len(list(str(n)))

count = 0
for i in range(1,1001):
    f = frac_expansion1(i)
    if(digit_count(f.numerator) > digit_count(f.denominator)):
        count += 1

print(count)