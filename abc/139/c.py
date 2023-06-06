N = int(input())
H = list(map(int,input().split()))
tmp = H[0]
flg = 0
cnt = -1
ans = 0

for i in range(N):
    #print(H[i], tmp)
    if tmp >= H[i]:
        if flg == 0:
            cnt += 1
            flg = 1
            tmp = H[i]
        else:
            cnt += 1
            tmp = H[i]
    else:
        flg = 0
        ans = max(ans, cnt)
        cnt = 0
        tmp = H[i]

ans = max(ans, cnt)

print(ans)    