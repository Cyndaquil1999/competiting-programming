from math import floor

N = int(input())

for num in range(1, 50001):
    if floor(num * 1.08) == N:
        exit(print(num))
        
print(":(")