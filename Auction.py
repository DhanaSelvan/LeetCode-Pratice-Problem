t = int(input())
for i in range(t):
    A, B, C = map(int, input().split())
    if(A!=B and B!=C and A!=C):
        if(A>B and A>C):
            print("Alice")
        elif(B>A and B>C):
            print("Bob")
        else:
            print("Charlie")