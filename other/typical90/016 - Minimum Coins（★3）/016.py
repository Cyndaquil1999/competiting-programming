N = int(input())
A, B, C = map(int,input().split())
ans = 10000
L = 10000

for a in range(L):
    for b in range(L):
        if N - A*a - B*b >= 0 and (N - A*a - B*b) % C == 0:
            c = (N - A*a - B*b) // C
            ans = min(ans, a + b + c)
            #print(a, b, c)

print(ans)