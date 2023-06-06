N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))
diff = 10**18
ans = 0

for i in range(N):
    if abs(A - (T - H[i]*0.006)) < diff:
        diff = abs(A - (T - H[i]*0.006))
        ans = i
    
print(ans+1)