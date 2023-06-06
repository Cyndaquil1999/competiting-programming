from itertools import permutations

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

p_idx = 0
q_idx = 0

li = list(permutations(range(1,N+1)))

for i in range(len(li)):
    if li[i] == P:
        p_idx = i
    
    if li[i] == Q:
        q_idx = i

print(abs(p_idx - q_idx))