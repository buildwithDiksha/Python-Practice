arr = [2,10,15,20,25,5,11]
# maximum element
max = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max = arr[i]
print("Maximum element is :",max)   

min = arr[0]
for i in range(1,len(arr)):
    if arr[i]<min:
        min = arr[i]
print("Smallest element : ",min)    

difference = max-min
print("Difference of maximum and minimum elements is : " , difference)