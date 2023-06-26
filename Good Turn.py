T = int(input())
for i in range(T):
    X, Y = map(int, input().split(" "))
    Sum = int(X) + int(Y)
    if (Sum>6):
        print("YES")
    else:
        print("NO")