t = int(input())
for i in range(t):
    List = []
    A,B,C = map(int, input().split(" "))
    a,b,c = int(A), int(B), int(C)
    List.append(a)
    List.append(b)
    List.append(c)
    List.remove(max(List))
    print(max(List))