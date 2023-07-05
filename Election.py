t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    final = []
    for j in a:
        if(j>=x):
            final.append(j)
    print(len(final))