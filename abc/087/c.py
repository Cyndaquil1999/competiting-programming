N = int(input())
A = [list(map(int,input().split())) for _ in range(2)]
ans = -1
for i in range(N):
    tmp = sum(A[0][:i+1]) + sum(A[1][i:])
    ans = max(ans, tmp)

print(ans)