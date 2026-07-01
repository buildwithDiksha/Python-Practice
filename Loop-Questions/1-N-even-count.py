N = int(input("Enter a number : "))
count = 0 
for i in range(1,N+1):
    if (i % 2 == 0):
        count = count+1
print(count)
