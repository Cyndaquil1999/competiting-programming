N = int(input())
S = input()

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if S[i] == "I" and S[j] == "O" and S[k] == "I":
                exit(print("Yes"))
                
print("No")