num1 = int(input("Enter 1st number: "))
operator = input("Enter operator -- (+, -, *, /) :-")
num2 = int(input("Enter 2nd number: "))

if (operator == "+"):
    print("Answer= ", (num1 + num2))

elif (operator == "-"):
    print("Answer= ", (num1 - num2))

elif (operator == "*"):
    print("Answer= ", (num1 * num2))

elif (operator == "/"):
    print("Answer= ", (num1 / num2))

else:
    print("Invalid Input.....")
