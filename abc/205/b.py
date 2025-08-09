N = int(input())
A = list(map(int, input().split()))

asc_A = sorted(A)

for i in range(N):
    if (i + 1 != asc_A[i]):
        print("No")
        exit()

print("Yes")