N = int(input())
A = list(map(int,input().split()))
ans = 0

while True:
    flg = False
    for i in range(N):
        if A[i] % 2 != 0:
            flg = True
            
    if flg:
        break
    
    for i in range(N):
        A[i] //= 2
    
    ans += 1
    
print(ans)