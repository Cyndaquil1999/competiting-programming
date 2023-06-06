S = input()
N = len(S)
cnt = 0

for i in range(N):
    if i == 0 and S[i] != "A":
        exit(print("WA"))
    elif (i == 2 or i == N-2) and S[i] == "C":
        cnt += 1
        continue
    elif i != 0 and i == 2 and i == N-2 and S[i].islower() == False:
        exit(print("WA"))

if cnt == 1:
    print("AC")
else:
    print("WA")        