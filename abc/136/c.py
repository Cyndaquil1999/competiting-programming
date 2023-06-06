N = int(input())
H = list(map(int,input().split()))

for i in range(N-1):
    if H[i] > H[i+1]:
        exit(print("No"))
    elif H[i] == H[i+1]:
        pass
    else:
        H[i+1] -= 1
print("Yes")