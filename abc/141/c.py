N, K, Q = map(int,input().split())
score = {i: 0 for i in range(N)}

for _ in range(Q):
    A = int(input())
    score[A-1] += 1

    
for key, val in score.items():
    if K-(Q-val) > 0:
        print("Yes")
    else:
        print("No")