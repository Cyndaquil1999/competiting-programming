S = input()

words = {}

for i in range(len(S)):
    if S[i] not in words:
        words[S[i]] = 1
    else:
        words[S[i]] += 1

for key, value in words.items():
    if value == 1:
        for i in range(len(S)):
            if S[i] == key:
                print(i + 1)
                
