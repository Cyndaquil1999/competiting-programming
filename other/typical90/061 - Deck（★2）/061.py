from collections import deque

numbers = deque()
Q = int(input())
for _ in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        numbers.appendleft(x)
    elif t == 2:
        numbers.append(x)
    else:
        print(numbers[x-1])