A, B, C, K = map(int,input().split())
ans = 0

if K % 2 == 0:
    ans = A - B
else:
    ans = B - A
    
if abs(ans) > 10**18:
    print("Unfair")
else:
    print(ans)