H, W = map(int,input().split())
A = [input() for _ in range(H)]

new_H = H + 2
new_W = W + 2
ans = [[""]*new_W for _ in range(new_H)]

for h in range(new_H):
    if h == 0 or h == new_H-1:
        ans[h] = "#"*new_W
        continue
    for w in range(new_W):
        if w == 0 or w == new_W-1:
            ans[h][w] = "#"
        else:
            ans[h][w] += A[h-1][w-1]
        
for i in range(len(ans)):
    if i != 0 and i != len(ans)-1:
        print("".join(ans[i]))
    else:
        print(ans[i])