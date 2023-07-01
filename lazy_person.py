t = int(input())
for i in range(t):
    x, m, d = map(int, input().split(" "))
    normal_time = int(x)
    chef_time = int(m)*int(x)
    limit = int(d)
    print(min(chef_time,normal_time+limit))