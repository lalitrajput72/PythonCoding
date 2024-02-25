import Operation

print("Add values : ", Operation.add(5,10))
print("Subtract values : ", Operation.subtract(5,10))
print("Multiply values : ", Operation.multiply(5,10))
print("Divide values : ", Operation.divide(5,10))

# use dir() to check all the function of an imported module
print(dir(Operation))
print(__name__)