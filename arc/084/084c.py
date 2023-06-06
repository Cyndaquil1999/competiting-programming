import bisect

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

ans = 0

for i in range(N):
    tmp_a = bisect.bisect_left(A, B[i])
    tmp_b = N - bisect.bisect_right(C, B[i])
    ans += tmp_a * tmp_b
    #print(tmp_a, tmp_b)
    
print(ans)