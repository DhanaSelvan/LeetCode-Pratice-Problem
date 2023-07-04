t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    first = a+b
    second = b+c
    thrid = a+c
    print(max(first, second, thrid))