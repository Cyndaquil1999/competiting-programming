a, b = input().split()

num = int(a + b)

for i in range(1,335):
    if num == i**2:
        exit(print("Yes"))

print("No")