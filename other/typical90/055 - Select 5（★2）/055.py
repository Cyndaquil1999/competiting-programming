N, P, Q = map(int,input().split())
A = list(map(int,input().split()))

ans = 0

for a in range(N-4):
    for b in range(a+1, N-3):
        for c in range(b+1, N-2):
            for d in range(c+1, N-1):
                for e in range(d+1, N):
                    if (((((A[a] % P) * A[b] % P) * A[c] % P) * A[d] % P) * A[e] % P) == Q:
                        ans += 1

print(ans)