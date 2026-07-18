arr = [10,30,44,3,98,65,91]
# smallest element
smallest = arr[0]
for i in range(1,len(arr)):
    if arr[i]<smallest:
        smallest = arr[i]

second = float('+inf')
for i in range(len(arr)):
    if arr[i]!=smallest and arr[i]<second:
        second = arr[i]
print(" Second smallest element is : " , second )        