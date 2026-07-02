N = 5 
# upper portion
for i in range(1,6):
    for k in range(N-i):
        print(" ",end = "")
    for j in range(2*i-1):
        print("*",end = "")
    print() 
# lower portion
for i in range(4,0,-1):
    for k in range(N-i):
        print(" ",end = "")
    for j in range(2*i-1):
        print("*",end = "")
    print()              