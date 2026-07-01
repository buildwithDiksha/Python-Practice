N = int(input("Enter a number : "))
for i in range(1,6):
    for k in range(N-i):
        print(" ",end ="")
    for j in range(i):
        print("*",end ="")
    print()    