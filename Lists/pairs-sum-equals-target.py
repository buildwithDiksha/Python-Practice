arr = [1,3,2,5,6,7,4]
target = 5
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])
    
