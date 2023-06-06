N = int(input())
A = list(map(int,input().split()))
A = sorted(A)
ans = 0

for i in range(1,N+1):
    idx = 3*N-2*i
    ans += A[idx]
    
print(ans)   