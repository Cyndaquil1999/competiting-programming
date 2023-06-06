N, Y = map(int,input().split())


#愚直に書くとTLE
for x in range(2001):
    for y in range(2001):
        #zはN,x,yが決まっているので一意に定まる
        z = N -(x+y)
        if z >= 0 and 10000*x + 5000*y + 1000*z == Y:
            exit(print(x,y,z))
            
print(-1,-1,-1)