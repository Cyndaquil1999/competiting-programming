N, T, P = map(int, input().split())
L = list(map(int, input().split()))
desc_L = sorted(L, reverse=True)

long_count = 0
for i in range(N):
    if (L[i] >= T):
        long_count += 1

# 既に条件を満たしている場合
if (long_count >= P):
    exit(print(0))
    
print(T - desc_L[P-1])