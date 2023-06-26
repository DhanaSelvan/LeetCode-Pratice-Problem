T = int(input())
for i in range(T):
    X, Y, A = map(int, input().split(" "))
    
    if((int(A) >= int(X)) and (int(A) < int(Y))):
        print("YES")
    else:
        print("NO")