A, B = map(int,input().split())

if A <= 0 and B >= 0:
    print("Zero")
elif A < 0 and B < 0:
    if (abs(A) - abs(B) + 1) % 2 == 0:
        print("Positive")
    else:
        print("Negative")
    
else:
    print("Positive")