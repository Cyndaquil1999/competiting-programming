import bisect

N, K = map(int,input().split())
a = list(map(int,input().split()))
b = sorted(list(map(int,input().split())))

def check(x):
    cnt = 0
    for i in range(N):
        cnt += bisect.bisect_right(b, x // a[i])
    
    return cnt >= K

left = 0
right = 10**19

while right - left > 1:
    mid = (right + left) // 2
    if check(mid):
        right = mid
    else:
        left = mid
        
print(right)