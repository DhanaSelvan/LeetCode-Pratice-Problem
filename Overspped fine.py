t = int(input())
for i in range(t):
    speed = int(input())
    if(speed<=70):
        print(0)
    elif(speed>70 and speed<=100):
        print(500)
    else:
        print(2000)