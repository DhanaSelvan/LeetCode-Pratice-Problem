t = int(input())
for i in range(t):
    hard, carbon, tensile = map(int, input().split(" "))
    if(hard>50 and carbon<0.7 and tensile>5600):
        print(10)
    elif(hard>50 and carbon<0.7):
        print(9)
    elif(carbon<0.7 and tensile>5600):
        print(8)
    elif(hard>50 and tensile>5600):
        print(7)
    elif(hard>50 or carbon<0.7 or tensile>5600):
        print(6)
    else:
        print(5)