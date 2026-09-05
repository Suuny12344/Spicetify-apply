#Calculator
#You are not supposed to see this!
operator = input("Enter an operator (+, -, /, *): ")
Num1 = float(input("Enter the first Number: "))
Num2 = float(input("Enter the second Number: "))

if operator == "+":
    result = Num1 + Num2
    print(round(result, 2))
elif operator =="-":
    result = Num1 - Num2
    print(round(result, 2))
elif operator =="/":
    result = Num1 / Num2
    print(round(result, 2))
elif operator =="*":
    result = Num1 * Num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator!")
