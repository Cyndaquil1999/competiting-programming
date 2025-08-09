N, K = map(int, input().split())
p = list(map(int, input().split()))

sorted_p = sorted(p)
print(sum(sorted_p[:K]))