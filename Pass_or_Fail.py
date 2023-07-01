t = int(input())
for i in range(t):
    N, X, P = map(int, input().split(" "))
    Correct = int(X)*3
    Incorrect = (int(N)-int(X))*-1
    final = Correct + Incorrect
    if(final>=int(P)):
        print("PASS")
    else:
        print("FAIL")