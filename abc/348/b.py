def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)**.5


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    max_length = -1
    answer = -1
    for j in range(N):
        if i == j:
            continue

        if max_length < calculate_distance(points[i], points[j]):
            max_length = calculate_distance(points[i], points[j])
            answer = max(answer, j + 1)
    print(answer)
