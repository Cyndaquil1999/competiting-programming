N = int(input())
X = list(map(int, input().split()))

asc_X = sorted(X)
print(sum(asc_X[N:4*N]) / (3 * N))