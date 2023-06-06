N, M = map(int,input().split())
Questions = [False]*N
Penalties  =[0]*N
Corrected = 0
Penalty = 0

for _ in range(M):
    P, S = input().split()
    P = int(P)
    
    if Questions[P-1] == False:
        if S == "WA":
            Penalties[P-1] += 1
        else:
            Corrected += 1
            Questions[P-1] = True
            Penalty += Penalties[P-1]
        
    else:
        pass
    
print(Corrected, Penalty)