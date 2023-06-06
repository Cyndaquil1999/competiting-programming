def f(x):
    x = str(x)
    total = 0
    for i in x:
        total += int(i)
    return total

N = int(input())
l = len(str(N))

