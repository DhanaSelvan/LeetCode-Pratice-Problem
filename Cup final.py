t = int(input())
for i in range(t):
    x, y, d = map(int, input().split())
    value = abs(x-y)
    if(value<=d):
        print("YES")
    else:
        print("NO")