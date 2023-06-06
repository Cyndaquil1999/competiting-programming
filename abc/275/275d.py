import sys
sys.setrecursionlimit(10**8)

def f(x):
    if x == 0:
        return 1
    elif x in memo:
        return memo[x]
    else:
        memo[x] = f(x//3) + f(x//2)
        return memo[x]


N = int(input())
memo = {0: 1}

print(f(N))