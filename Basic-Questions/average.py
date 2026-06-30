sub1 = int(input("Enter marks of subject1 : "))
sub2 = int(input("Enter marks of subject2 : "))
sub3 = int(input("Enter marks of subject3 : "))
average = (sub1+sub2+sub3)/3
print(f"Average : {average:.2f}")

if sub1 >= 40  and  sub2 >= 40  and sub3 >= 40 :  
    print("pass")
else:
    print("fail")    