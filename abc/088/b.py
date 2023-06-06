N = int(input())
A = sorted(list(map(int,input().split())), reverse=True)
ans = 0

for i in range(N):
    if i % 2 == 0:
        ans += A[i]
    else:
        ans -= A[i]
    
print(ans)