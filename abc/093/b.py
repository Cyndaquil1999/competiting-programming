A, B, K = map(int,input().split())

for num in range(A, B+1):
    if num <= A+K-1 or num >= B-K+1:
        print(num)