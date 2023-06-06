N, M = map(int,input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int,input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)


for i in range(len(G)):
    print(len(G[i]))