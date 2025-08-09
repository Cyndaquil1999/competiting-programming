N = int(input())
A = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    new_A = []
    for j in range(i):
        new_A.append(abs(A[j] - A[j+1]))

    A = new_A

print(*new_A)