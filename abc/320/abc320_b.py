def is_palindrome(S):
    return S == S[::-1]


S = input()

answer = 0
for i in range(len(S)+1):
    for j in range(i):
        if i-j == 1:
            answer = max(answer, 1)
            continue
        if is_palindrome(S[j:i]):
            answer = max(answer, i - j)
print(answer)
