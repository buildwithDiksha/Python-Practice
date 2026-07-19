arr = [1,2,3,3,4,5,5,6,6,5,4]
duplicate = []

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicate:
            duplicate.append(arr[i])
print(duplicate)            