X = int(input())
Q = X // 100
T = X % 100

if 5 * Q < T:
    print(0)
else:
    print(1)