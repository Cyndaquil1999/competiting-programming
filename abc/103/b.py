from collections import deque
S = input()
T = input()
d = deque(S)
ans = "No"

for _ in range(len(S)):
    tmp = d.pop()
    d.appendleft(tmp)
    if "".join(list(d)) == T:
        ans = "Yes"
        break

print(ans)