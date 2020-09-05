# Get numbers from user
num1, num2 = input('enter 2 numbers: ').split()

# Converts strings to regular numbers
num1 = int(num1)
num2 = int(num2)

# Adds values and stores in sum
sum = num1 + num2

# Subtract values and stores in difference
difference = num1 - num2

# Multiply values and stores in product
product = num1 * num2

# Divide, store into quotient
quotient = num1 / num2

#use modulus for remainder
remainder = num1 % num2

# Print out everything
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
