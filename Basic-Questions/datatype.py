num = input("Enter a number : ") 
try :
    value = int(num)
    print("Integer")
    print(type(value))
except ValueError:
    value = float(num)
    print("Float")
    print(type(value))