N, M = map(int,input().split())
fav = {i: 0 for i in range(M+1)}
ans = 0

for _ in range(N):
    data = list(map(int,input().split()))
    for i in range(1, len(data)):
        fav[data[i]] += 1
    
for key, val in fav.items():
    if val == N:
        ans += 1
        
print(ans)