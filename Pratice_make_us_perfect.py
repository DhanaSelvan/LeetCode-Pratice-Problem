p = list(map(int, input().split(" ")))
List = []
for i in p:
    if(i>=10):
        List.append(i)
print(len(List))