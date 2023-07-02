t = int(input())
for i in range(t):
    x, y = map(int, input().split(" "))
    if(int(x)!=int(y)):
        if(int(x)>int(y)):
            print("A")
        else:
            print("B")