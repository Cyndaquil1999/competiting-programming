N, D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
ans = 0

for Y in range(N-1):
    for Z in range(Y+1, N):
        tmp = 0
        for y, z in zip(X[Y], X[Z]):
            tmp += (y-z)**2
        
        tmp = tmp**.5
        if tmp.is_integer():
            ans += 1

print(ans)