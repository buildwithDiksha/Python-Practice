arr = [10,20,60,40,99] ;
# largest element
largest = arr[0]
for i in range(1,len(arr)):
    if arr[i]>largest:
        largest = arr[i]

# second largest
second = float('-inf')
for i in range(len(arr)):
    if arr[i]!=largest and arr[i]>second:
        second = arr[i]

print("Second largest element : " , second)
