N = int(input())
d = list(map(int, input().split()))

answer = 0

for i in range(N-1):
    for j in range(i+1, N):
        answer += d[i] * d[j]

print(answer)
