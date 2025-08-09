N = int(input())
A = list(map(int, input().split()))

answer = []

for i in range(N-1):
    answer.append(A[i])
    if abs(A[i+1] - A[i]) != 1:
        if A[i] < A[i+1]:
            for j in range(A[i] + 1, A[i+1]):
                answer.append(j)
        elif A[i] > A[i+1]:
            for j in range(A[i]-1, A[i+1], -1):
                answer.append(j)
        else:
            continue
        
answer.append(A[-1])
print(*answer)