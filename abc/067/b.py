N, K = map(int, input().split())
L = list(map(int, input().split()))

desc_L = sorted(L, reverse=True)
print(sum(desc_L[:K]))