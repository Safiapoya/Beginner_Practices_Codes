temp = float(input("Enter the temperature value:\n "))
unit = input("Select the unit of measurement(C or F):\n")
if unit.upper() == "C":
    converted_temp = (temp*9/5)+32
    print("The temperature in Celsius is: {:.2f} ".format(converted_temp))
elif unit.upper() == "F":
    converted_temp = (temp-32)*9/5
    print("The temperature in Fahrenheit is: {:.2f}".format(converted_temp))
else:
    print("Invalid unit input.please enter 'C' for Celsius or 'F' for Fahrenheit.")

