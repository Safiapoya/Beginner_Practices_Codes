num1 = float(input("Please enter your number:\n"))
num2 = float(input("Enter your next number:\n"))
operation = input("What operation do you want apply: +\t-\t*\t/\t%\n")
result = 0
if operation == "+":
    result = num1+num2
elif operation == "-":
    result = num1-num2
elif operation == "*":
    result = num1*num2
elif operation == "/":
    result = num1/num2
else:
    print("Invalid operator!")

if operation in ["+", "-", "*", "/"]:
    print("The result is: {:.2f}".format(result))

