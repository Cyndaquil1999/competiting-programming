N = int(input())
words = dict()
tail = ""
flg = True

for i in range(N):
    W = input()
    
    if W not in words and flg:
        words[W] = 1
    else:
        flg = False
    
    if i != 0 and W[0] != tail and flg:
        flg = False
    
    tail = W[-1]

if flg:
    print("Yes")
else:
    print("No")