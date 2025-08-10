S = input()
check = {}

for s in S:
    if s not in check:
        check[s] = 1
    else:
        exit(print("no"))

print("yes")
