N, A, B = map(int,input().split())
ans = 0

if A % 2 == B % 2:
    ans = (B-A) // 2

else:
    ans = min((A+B-1)//2, (N*2-A-B+1)//2) 
    
print(ans)