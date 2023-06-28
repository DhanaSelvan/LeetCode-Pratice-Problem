t = int(input())
for i in range(t):
    wallet, bill = map(int, input().split(" "))
    if(bill<=wallet):
        print("YES")
    else:
        print("NO")