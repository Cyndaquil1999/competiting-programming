N = int(input())
data = []

for i in range(N):
    S, P = input().split()
    data.append([S, int(P)])

data = sorted(data, key=lambda x: (x[0], -x[1]))
print(data)