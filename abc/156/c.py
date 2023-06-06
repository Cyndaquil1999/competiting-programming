from math import floor, ceil

N = int(input())
X = list(map(int,input().split()))

average_xs = [floor(sum(X)/N), ceil(sum(X)/N)]
cost = 10**18


for average_x in average_xs:
    cost_tmp = 0
    for x in X:
        cost_tmp += (x - average_x)**2
    
    cost = min(cost, cost_tmp)
    
    
print(cost)