def f(x):
    if x % 10 != 0:
        t = x % 10
        return x + 10 - t
    return x

from itertools import permutations
menu = [int(input()) for _ in range(5)]
ans = 10**3
orders = list(permutations(menu))

for order in orders:
    tmp = 0
    for i in range(4):
        tmp += f(order[i])
        
    tmp += order[4]
    #print(order, tmp)
        
    ans = min(ans, tmp)
print(ans)