def divisors(x):
    num = []
    for i in range(1, int(x**.5)+1):
        if x % i == 0:
            num.append(i)
            if x // i != i:
                num.append(x // i)
            
    return sorted(num)

N = int(input())
divisors_list = divisors(N)
ans = 10**18

l = len(divisors_list)
for i in range(l):
    if i >= l-1-i:
        ans = min(ans, divisors_list[i] + divisors_list[l-1-i] - 2)
    else:
        pass
    
print(ans)