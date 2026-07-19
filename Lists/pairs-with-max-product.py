arr = [ 1,2,3,4,5]
max_product = float('-inf')
pair = ()

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]*arr[j]>max_product:
            max_product = arr[i]*arr[j]
            pair = arr[i],arr[j]
print("Maximum product pairs are :", pair)    