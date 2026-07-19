arr = [1,2,3,4,5,6,7,8]
arr1= []
arr2 = []

for i in range(len(arr)):
    if i % 2==0:
        arr1.append(arr[i])
print(arr1)
for j in range(len(arr)):
    if j % 2 != 0:
        arr2.append(arr[j])
print(arr2)
