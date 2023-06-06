H, W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [[0 for _ in range(W)] for _ in range(H)]

#列成分の計算
cols = [0 for _ in range(W)]
for j in range(W):
    for i in range(H):
        cols[j] += A[i][j]
        

#行成分の計算
rows = [0 for _ in range(H)]
for i in range(H):
    for j in range(W):
        rows[i] += A[i][j]
        
#Bに代入する
for i in range(H):
    for j in range(W):
        B[i][j] = rows[i] + cols[j] - A[i][j]
        
        
for i in range(H):
    print(*B[i])