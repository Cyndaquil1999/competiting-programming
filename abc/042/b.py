N, L = map(int,input().split())
words = []

for _ in range(N):
    S = input()
    words.append(S)

print("".join(sorted(words)))