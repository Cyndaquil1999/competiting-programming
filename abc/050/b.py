N = int(input())
T = list(map(int,input().split()))
total = sum(T)
M = int(input())
for _ in range(M):
    ans = total
    P, X = map(int,input().split())
    ans = ans - T[P-1] + X
    print(ans)