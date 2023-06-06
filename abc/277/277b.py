N = int(input())

memo = set()

for _ in range(N):
    S = input()
    memo.add(S)
    
    
    if S[0] in ["H", "D", "C", "S"] and S[1] in ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K"]:
        