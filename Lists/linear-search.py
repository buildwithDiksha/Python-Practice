arr = [20,30,40,50]
target = 40
found = False

for x in arr:
    if x == target:
        found = True
        break

if found:
    print("Target found",target)
else:
    print("Target not found")    

