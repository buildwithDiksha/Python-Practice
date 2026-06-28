num = 121 ;
reverse = 0 ;
original_num = num ;

while num > 0 :
    digit = num % 10
    reverse = reverse*10+digit
    num = num // 10 

print("Reverse number :" , reverse)

if reverse==original_num:
    print("palindrome number")
    
else:
    print("not a palindrome number")

