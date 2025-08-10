N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

answer = 10**18

for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        # maxで比較すると遅くなるのでTLE
        if distance < answer:
            answer = distance

print(answer)
