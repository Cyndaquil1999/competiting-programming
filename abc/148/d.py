N = int(input())
A = list(map(int,input().split()))
cnt = 1

for i in range(N):
    if A[i] == cnt:
        cnt += 1
    
if cnt == 1:
    print(-1)
else:
    print(N - cnt + 1)