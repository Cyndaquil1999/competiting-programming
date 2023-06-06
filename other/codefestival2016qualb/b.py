N, A, B = map(int,input().split())
S = input()

pass_count = 0
b_count = 1

for s in S:
    if s == "a" and pass_count < A+B:
        print("Yes")
        pass_count += 1
        
    elif s == "b" and pass_count < A+B and b_count <= B:
        print("Yes")
        pass_count += 1
        b_count += 1
    
    else:
        print("No")