N = int(input())
time = [list(map(int,input().split())) for _ in range(N)]
left = 0
right = 10**18

while right - left > 1:
    mid = (right + left) // 2
    
    flg = True
    t = [0]*N
    
    for i in range(N):
        if mid < time[i][0]:
            flg = False
        else:
            t[i] = (mid - time[i][0]) // time[i][1]
        
    t.sort()
    for i in range(N):
        if t[i] < i:
            flg = False
            
    if flg:
        right = mid
    else:
        left = mid
        
print(right)