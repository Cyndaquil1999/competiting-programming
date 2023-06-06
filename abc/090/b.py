def is_palindromic(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

A, B = map(int,input().split())
ans = 0

for x in range(A, B+1):
    if is_palindromic(x):
        ans += 1

print(ans)