# Q3. Float ko int mein convert karo aur difference print karo
#  Example: 7.9 → 7 (kya lose hua?)


num = float(input("Enter a number : "))
value = int(num)
difference = num - value 

print("Original Float Number : " , num)
print("Converted Number : " , value )
print("Difference : " , difference)