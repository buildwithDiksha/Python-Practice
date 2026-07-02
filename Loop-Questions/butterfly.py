N = 4
    # upper portion
for i in range(1,N):
    for j in range(i):
        print("*",end = "")
    # middle spaces
    for k in range(2*(N-i)):
        print(" ",end ="")    
    for l in range(i):
        print("*",end = "")
    print()
    # middle portion
for i in range(1,N-1):
    for j in range(1,9):
        print("*",end = "")
    print()    
    # lower portion
for i in range(3,0,-1):
    for j in range(i):
        print("*",end ="")
    for k in range (2*(N-i)):
        print(" ",end = "")
    for l in range(i):
        print("*",end ="")
    print()                