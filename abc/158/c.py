A, B = map(int,input().split())
for i in range(1,1501):
    if (i * 0.08)//1 == A and (i * 0.1) // 1 == B:
        exit(print(i))
        
print(-1)