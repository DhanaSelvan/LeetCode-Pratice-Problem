t = int(input())
for i in range(t):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    best1, best2 = max(a1, a2), max(a2,a3)
    best3, best4= max(b1,b2), max(b3,b2)
    besta = best1+best2
    bestb = best3+best4
    if(besta>bestb):
        print("Alice")
    elif(besta<bestb):
        print("Bob")
    else:
        print("Tie")
        
# Another way
t = int(input())
for i in range(t):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    x = sorted([a1,a2,a3])
    y = sorted([b1,b2,b3])
    besta = x[-1] + x[-2]
    bestb = y[-1] + y[-2]
    if(besta>bestb):
        print("Alice")
    elif(besta<bestb):
        print("Bob")
    else:
        print("Tie")