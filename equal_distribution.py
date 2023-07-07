t = int(input())
for i in range(t):
    A, B = map(int, input().split())
    Add = A + B
    if(Add%2==0):
        print("YES")
    else:
        print("NO")