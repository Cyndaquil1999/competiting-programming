N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0

# Aを1つ決めた時にその値がBに含まれていればインクリメント
for a in A:
    if a in B:
        answer += 1

print(answer)