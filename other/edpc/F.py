s = input()
t = input()

dp = [[0]*(len(t)+1) for i in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j] and i != 0 and j != 0:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
print(dp)

#復元処理    
ans = []
i = 0
j = 0

"""
while i < len(s) and j < len(t):
    
    print(i,j)

    if s[i] == t[j]:
        ans.append(s[i])
        i += 1
        j += 1
        
    elif dp[i][j] == dp[i+1][j]:
        i += 1
    elif dp[i][j] == dp[i][j+1]:
        j += 1
"""
print(ans)