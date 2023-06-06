A, B, C, X, Y = map(int,input().split())

if A + B <= 2*C:
    ans = A*X + B*Y
else:
    if X <= Y:
        ans = min(2*X*C + B*(Y-X), 2*Y*C)
    else:
        ans = min(2*Y*C + A*(X-Y), 2*X*C)

print(ans)

