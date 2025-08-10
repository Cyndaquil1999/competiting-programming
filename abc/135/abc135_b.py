N = int(input())
P = list(map(int, input().split()))

asc_P = sorted(P)

answer = "NO"

if P == asc_P:
    answer = "YES"

for i in range(N):
    for j in range(i + 1, N):
        P[i], P[j] = P[j], P[i]
        
        if asc_P == P:
            answer = "YES"
        
        P[i], P[j] = P[j], P[i]

print(answer)