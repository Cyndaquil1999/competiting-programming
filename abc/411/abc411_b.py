N = int(input())
D = list(map(int, input().split()))


def calculate_distances(D, start):
    distances = [D[start]]
    for i in range(start + 1, len(D)):
        distances.append(distances[-1] + D[i])
    return distances


for i in range(N - 1):
    print(*calculate_distances(D, i))
