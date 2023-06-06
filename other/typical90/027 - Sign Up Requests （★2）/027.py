N = int(input())
checked = set()

for i in range(N):
    S = input()
    if S not in checked:
        print(i+1)
        checked.add(S)
    
    else:
        pass