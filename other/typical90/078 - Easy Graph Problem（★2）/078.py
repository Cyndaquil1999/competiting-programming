N, M = map(int,input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    G[a-1].append(b)
    G[b-1].append(a)

G = [sorted(i) for i in G]
ans = 0

for i in range(N):
    if len(G[i]) >= 2:
        if G[i][0] < i+1 and i+1 < G[i][1]:
            ans += 1

    elif len(G[i]) == 1 and G[i][0] < i+1:
        ans += 1
    
        

print(ans)