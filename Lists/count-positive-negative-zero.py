arr = [ 1,2,0,-3,-34,-5,7,9,5,0]
pos = 0
neg = 0 
zero = 0
for x in arr:
    if x>0 :
        pos = pos+1
    if x<0:
        neg = neg+1
    if x==0:
        zero = zero+1        
print("postive numbers : ",pos)      
print("negative numbers : ",neg)      
print("zeros : ",zero)        