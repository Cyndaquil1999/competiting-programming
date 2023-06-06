N = int(input())
words = dict()

for _ in range(N):
    S = input()
    if S not in words:
        words[S] = 1
    else:
        words[S] += 1

tmp = sorted(words.items(), key=lambda x: x[1], reverse=True)
max_val = tmp[0][1]

ans = []
for i in tmp:
    if i[1] == max_val:
        ans.append(i[0])

ans = sorted(ans)

for i in ans:
    print(i)