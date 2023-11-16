num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))
operator = input("Do you want to add or multiply these numbers?")
if operator == "add":
    print(num1+num2)
elif operator == "multiply":
    print(num1*num2)
else:
    print("Wrong answer")
