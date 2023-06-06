def f(x):
    res = []
    
    for num in range(2, x):
        if num ** 2 > x:
            break
        
        if x % num != 0:
            continue
        
        e = 0
        while x % num == 0:
            e += 1
            x //= num
            
        res.append((num, e))
        
    if x != 1:
        res.append((x, 1))
    return res

N = int(input())
A = list(map(int,input().split()))
ans = 0

for a in A:
    tmp = f(a)
    if tmp[0][0] == 2:
        ans += tmp[0][1]

print(ans)