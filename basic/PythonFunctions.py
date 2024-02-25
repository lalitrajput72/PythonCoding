from multipledispatch import dispatch

@dispatch()
def dance():
    print("lets dance")

# function with argument
@dispatch(int)
def dance(name):
    print("lets count : ", name)

dance()
dance(5)

# The problem with method overloading in
# Python is that we may overload the methods but can only call the latest defined method.

# This problem can be solved by multiple dispatch decorator

# Run pip3 install multipledispatch

# Function arguments with default value
def sum(a=5, b=10):
    return a+b

print(sum())
print(sum(4))
print(sum(4,4))

# Function call with keyword arguments
def printName(firstName, lastName):
    print(firstName + lastName)

printName(lastName="Rajput", firstName="Lalit ")

# Arbitrary Arguments
def receive(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print(sum)

receive(5, 10, 15, 10, 10)
