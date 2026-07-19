arr = [2,3,4,2,5,6,7,6,2,3]
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count = count+1
    print(arr[i],"occurs",count,"times")            

