from itertools import accumulate

N = int(input())
class_1 = [0] * (N+1)
class_2 = [0] * (N+1)

for i in range(N):
    C, P = map(int,input().split())
    if C == 1:
        class_1[i+1] = P
    else:
        class_2[i+1] = P

cumsum_1 = list(accumulate(class_1))
cumsum_2 = list(accumulate(class_2))


#print(cumsum_1, cumsum_2)
#print(class_1, class_2)

Q = int(input())
for _ in range(Q):
    L, R = map(int,input().split())
    print(cumsum_1[R] - cumsum_1[L-1], cumsum_2[R] - cumsum_2[L-1])
