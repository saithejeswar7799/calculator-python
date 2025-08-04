def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a/b
    else:
        return "Erroe!division by zero"
def calculator():
    while True:
        print("Select Operations:")
        print("1.Addition")
        print("2.Substraction")
        print("3.Multipy")
        print("4.Division")
        print("5.Exit")
        user_choice=int(input("Enter user choice:"))
        if user_choice==5:
           print("exciting cleanly..")
           break  #exit the loop
        num1=int(input("enter number1:"))
        num2=int(input("enter number2:"))
        if user_choice==1:
           print(f"Result:{num1}+{num2}={add(num1,num2)}")
        elif user_choice==2:
            print(f"Result:{num1}-{num2}={subtract(num1,num2)}")
        elif user_choice==3:
            print(f"Result:{num1}*{num2}={multiply(num1,num2)}")
        elif user_choice==4:      
            print(f"Result:{num1}/{num2}={division(num1,num2)}")
        else:
            print(f"Invalid Operations..")
    
calculator()
    
