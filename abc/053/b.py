S = input()
ans = 0
tmp = 0
flg = False

for i in range(len(S)):
    if S[i] == "A" and flg == False:
        tmp = i
        flg = True
    
    if S[i] == "Z":
        ans = max(ans, i - tmp)
        flg = False
        
print(ans+1) 