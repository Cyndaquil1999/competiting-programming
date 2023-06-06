def f(x):
    if memo[x] != -1:
        return memo[x]
    
    if x == 0:
        return 2
    
    elif x == 1:
        return 1
    
    memo[x] = f(x-1) + f(x-2)
    return memo[x]

N = int(input())
memo = [-1] * (N+1)

print(f(N))