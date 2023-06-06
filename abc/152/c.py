N = int(input())
P = list(map(int,input().split()))
ans = 1
min_num = P[0]

for i in range(1,N):
    min_num = min(min_num, P[i])
    
    if P[i] == min_num:
        ans += 1
        #print(i+1, ans) 
    

print(ans)