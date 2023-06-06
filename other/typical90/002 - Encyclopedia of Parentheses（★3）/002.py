N = int(input())
ans = []

for i in range(2 ** N):
    diff = 0
    S = ''
    for j in range(N):
        if (i >> j) & 1:
           diff -= 1
           S += ')'
        else:
            diff += 1
            S += '('

        if diff < 0:
            break

    if diff == 0:
        ans.append(S)

for i in sorted(ans):
    print(i)