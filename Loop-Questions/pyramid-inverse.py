N = 5 
for i in range(5,0,-1):
    for k in range(N-i):
        print(" ",end = "")
    for j in range(2*i-1):
        print("*",end ="")
    print()        