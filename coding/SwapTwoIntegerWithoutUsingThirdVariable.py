# Ask user to enter 2 numbers
a = float(input("Enter first number : "))
b = float(input("Enter first number : "))

a = a + b
b = a - b
a = a - b

#print output
print("First number is : {0} and second number is : {1}".format(a, b))

# Python has another construct to swap the variable
# a, b = b, a