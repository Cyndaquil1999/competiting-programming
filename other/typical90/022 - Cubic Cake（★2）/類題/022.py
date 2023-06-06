from functools import reduce
from math import gcd

def get_gcds(*integers):
    return reduce(gcd, integers)

A, B, C = map(int,input().split())
g = get_gcds(A, B, C)

if g == 1:
    print(A + B + C - 3)
    
else:
    print(A // g + B // g + C // g - 3)