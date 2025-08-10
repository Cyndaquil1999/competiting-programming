N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = set(map(int, input().split()))

dic = {}
for a in A:
    if a not in dic:
        dic[a] = 1
    else: 
        dic[a] += 1

answer = 0

for key in B:
    answer += dic.get(key, 0)

print(answer)