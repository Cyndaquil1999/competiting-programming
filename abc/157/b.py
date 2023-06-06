A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())

card = [[0 for _ in range(3)] for _ in range(3)]
#print(card)

for _ in range(N):
    b = int(input())
    
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                card[i][j] = 1
        
#縦の処理
tmp = 0
for j in range(3):
    for i in range(3):
        tmp += card[i][j]
        if tmp % 3 == 0 and tmp != 0:
            exit(print("Yes"))
            
#横の処理
tmp = 0
for i in range(3):
    for j in range(3):
        tmp += card[i][j]
        if tmp % 3 == 0 and tmp != 0:
            exit(print("Yes"))
            
#斜めの処理
if card[0][0] + card[1][1] + card[2][2] == 3 or card[0][2] + card[1][1] + card[2][0] == 3:
    exit(print("Yes"))

print("No")