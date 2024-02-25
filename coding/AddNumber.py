# Add given two numbers

num1 = 20
num2 = 30.0

sum = num1 + num2

# Learning 1
# You don't have to give datatype of the number, it automatically maps based upon value you have provided.
# Also does the type casting for you
# Gives you error at runtime if type casting is not possible


# Print the sum of the number
print(sum)

# Print the sum in formatted form
print("Sum of number {0} and {1} is {2}".format(num1, num2, sum))

# Add Number With User Input
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
# input functions returns a string, so using float function below before adding to change it in to
# number format

sum = float(num1) + float(num2);
# display the sum
print("Sum of number {0} and {1} is {2}".format(num1, num2, sum))