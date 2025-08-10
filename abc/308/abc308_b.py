N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

answer = 0

for c in C:
    if c in D:
        answer += P[D.index(c) + 1]
    else:
        answer += P[0]

print(answer)
