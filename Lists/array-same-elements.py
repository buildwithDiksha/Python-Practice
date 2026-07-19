arr1 = [1,2,3,4]
arr2 = [1,2,3,4]
found = True

if len(arr1) != len(arr2):
    found = False
else:
    for i in range(len(arr1)):
        found = False
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                found = True
                break ;
        if not found:
            found = False 
            break
                        
print("They contain same elements : ",found)
