import math

def f(t):
    return A * t + B * math.sin(C * t * math.pi)

A, B, C = map(int,input().split())

eps = 10 ** (-9)
l = 0
m = -1
r = 200

while abs(f(m) - 100) > eps:
    m = (l + r) / 2
    
    if f(m) >= 100:
        r = m
    else:
        l = m
        
print(m)