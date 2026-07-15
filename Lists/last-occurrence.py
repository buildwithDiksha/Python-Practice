arr = [10,20,40,30,40,50,60]
target = 40
for i in range(len(arr)-1,-1,-1):
    if arr[i]==target:
        print("Last occurrence of",target,"is at index : ",i)
        break