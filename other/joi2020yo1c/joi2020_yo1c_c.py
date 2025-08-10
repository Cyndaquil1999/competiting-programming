N = int(input())
A = list(map(int, input().split()))

answer = 1
tmp = 1

for i in range(1, N):
    if (A[i] >= A[i - 1]):
        tmp += 1
    else:
        tmp = 1

    answer = max(answer, tmp)

print(answer)
