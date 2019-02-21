# calculator app

# user inputs two numbers and operator
num1, operator, num2 = input('Enter calculation: ').split()

# strings to integters
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "-":
    print("{} / {} = {}".format(num1, num2, num1/num2))
else:
	print("This small app can only hanlde simple math operators: + - * /")