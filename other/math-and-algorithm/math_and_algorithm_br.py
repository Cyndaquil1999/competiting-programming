N, X = map(int, input().split())

answer = 0

for a in range(1, N - 1):
    for b in range(a+1, N):
        for c in range(b+1, N + 1):
            if a + b + c == X:
                answer += 1

print(answer)
