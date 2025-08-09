N, K = map(int, input().split())
S = [input() for _ in range(N)]

split_S = sorted(S[:K])

for i in range(K):
    print(split_S[i])