arr = [1,2,3,4,3,5,6,3]
target = 3
new_arr = []
for num in arr:
    if num != target:
        new_arr.append(num)
print(new_arr)        
