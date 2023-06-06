def base_10(num_n, n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

N, K = map(int,input().split())
if N == 0:
    exit(print(0))

ans = base_n(base_10(N, 8),9)



if K == 1:
    new = ''
    for s in str(ans):
        if s == '8':
            new += '5'
        else:
            new += s

else:
    for _ in range(K-1):
        new = ''
        for s in str(ans):
            if s == '8':
                new += '5'
            else:
                new += s
            
        ans = base_n(base_10(int(new), 8),9)
    
    new = ''
    for s in str(ans):
        if s == '8':
            new += '5'
        else:
            new += s


print(new)