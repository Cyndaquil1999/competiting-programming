S = input()
tmp_1, tmp_2 = 0, 0

for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == "0":
            tmp_2 += 1
        else:
            tmp_1 += 1
        
    else:
        if S[i] == "1":
            tmp_2 += 1
        else:
            tmp_1 += 1
        
print(min(tmp_1, tmp_2))