N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = min(A[0], B[0])

for i in range(1,N):
    print(ans)
    ans += min(A[i], B[i]-min(A[i-1], B[i-1]))
print(ans)