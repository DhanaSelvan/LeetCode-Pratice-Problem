n = int(input())
array = list(map(str, input().split(" ")))
step = int(input())
for i in range(step):
    List = array[i+1:] + array[:i+1]
print(' '.join(List), end=" ")