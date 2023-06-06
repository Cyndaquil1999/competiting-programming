S = input()
ans = 0
N = len(S) - 1

for i in range(2**N):
    tmp = S[0]
    for j in range(N):
        if (i >> j) & 1:
            tmp += "+"
        tmp += S[j+1]
    ans += eval(tmp)
            
print(ans)