N = int(input("Enter a number : "))
for i in range(5,0,-1):
    for k in range(N-i):
        print(" ",end = "")
    for j in range(i):
        print("*",end = "")
    print()    