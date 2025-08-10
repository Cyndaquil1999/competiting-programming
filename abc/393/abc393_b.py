S = input()
N = len(S)
answer = 0

for i in range(N):
    if S[i] == "A":
        for j in range(i + 1, N):
            if S[j] == "B":
                diff = j - i
                
                for k in range(j + 1, N):
                    if S[k] == "C" and k - j == diff:
                        answer += 1

print(answer)