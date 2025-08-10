S = input()
N = len(S)
words = []

for i in range(N):
    words.append(S[i:] + S[:i])  
    
print(min(words))
print(max(words))