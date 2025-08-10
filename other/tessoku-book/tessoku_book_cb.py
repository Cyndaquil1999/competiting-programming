N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if k == i or k == j:
                continue

            if A[i] + A[j] + A[k] == 1000:
                exit(print("Yes"))

print("No")
