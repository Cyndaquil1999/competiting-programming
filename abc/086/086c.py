N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

diff = data[0][1] + data[0][2]

if (diff - data[0][0]) % 2 == 0 and diff <= data[0][0]:
    pass
else:
    exit(print("No"))

for i in range(N-1):
    t_s,x_s,y_s = data[i][0], data[i][1], data[i][2]
    t_g,x_g,y_g = data[i+1][0], data[i+1][1], data[i+1][2]
    
    diff = abs(x_g-x_s) + abs(y_g-y_s)
    diff_t = t_g-t_s
    if abs(diff_t - diff) % 2 == 0 and diff <= diff_t:
        pass
    else:
        exit(print("No"))
        
print("Yes")