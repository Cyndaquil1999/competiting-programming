N = int(input())
W = list(map(int, input().split()))

answer = 10**18

for T in range(N-1):
    S1 = sum(W[:T+1])
    S2 = sum(W[T+1:])
    
    answer = min(answer, abs(S1 - S2))
    
print(answer)
    