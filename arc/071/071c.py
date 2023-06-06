from collections import defaultdict

n = int(input())
ans = defaultdict(int)
for i in range(26):
    tmp = chr(ord("a") + i)
    ans[tmp] = 10000
    
res = ""

for i in range(n):
    S = input()

    for j in range(26):
        tmp = chr(ord("a") + j)
        ans[tmp] = min(ans[tmp], S.count(tmp))   
        
for idx, val in ans.items():
    res += idx * val
    
print(res)