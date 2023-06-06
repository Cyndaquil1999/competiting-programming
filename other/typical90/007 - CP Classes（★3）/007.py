from bisect import bisect

N = int(input())
A = sorted(list(map(int,input().split())))
Q = int(input())
#print(A)

for _ in range(Q):
    B = int(input())
    idx = bisect(A, B)
    #print(idx)

    if idx == 0:
        print(abs(A[idx]-B))
    elif idx == N:
        print(abs(A[idx-1]-B))
    else:
        print(min(abs(A[idx-1]-B), abs(A[idx]-B)))
