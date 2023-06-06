N = int(input())

for i in range(7):
    if 2**i <= N and 2**(i+1) > N:
        print(2**i)