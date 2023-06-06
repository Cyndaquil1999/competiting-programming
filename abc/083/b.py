def digit_sum(x):
    x = str(x)
    ans = 0
    for digit in x:
        ans += int(digit)
    return ans

N, A, B = map(int,input().split())
ans = 0

for num in range(1, N+1):
    tmp = digit_sum(num)
    if A <= tmp and tmp <= B:
        ans += num
        
print(ans)