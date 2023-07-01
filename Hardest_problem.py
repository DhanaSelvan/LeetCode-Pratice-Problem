t = int(input())
for i in range(t):
    a, b, c = map(int, input().split(" "))
    if(int(c)<int(b) and int(c)<int(a)):
        print("Alice")
    elif(int(b)<int(c) and int(b)<int(a)):
        print("Bob")
    else:
        print("Draw")