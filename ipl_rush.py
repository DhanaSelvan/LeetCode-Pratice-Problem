t = int(input())
for i in range(t):
    T, m = map(int, input().split(" "))
    if(T>=m):
        print(T-m)
    else:
        print(0)