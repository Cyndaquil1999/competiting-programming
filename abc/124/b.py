N = int(input())
H = list(map(int, input().split()))

answer = 0 
max_height = 0

for i in range(N):
    if H[i] >= max_height:
        answer += 1
        max_height = H[i]
    
print(answer)