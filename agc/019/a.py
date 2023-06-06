Q, H, S, D = map(int,input().split())
N = int(input())
ans = 0

tmp = N // 2
min_price2 = min(min(8*Q, 4*H), min(2*S, D))
min_price1 = min(min(4*Q, 2*H), S)

if N % 2 == 0:    
    ans = tmp * min_price2
else:
    ans = tmp * min_price2 + (N-tmp*2) * min_price1
    
print(ans)