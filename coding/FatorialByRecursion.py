# Lets solve factorial of a number using recursion in python

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))

# factorial(3)           1st call with 3
# 3 * factorial(2)       2nd call with 2
# 3 * 2 * factorial(1)   3rd call with 1
# 3 * 2 * 1              return from 3rd call as number=1
# 3 * 2                  return from 2nd call
# 6                      return from 1st call

# Here the base condition is num == 1, if it is not implemented than function will call
# recursively infinite times untill gets stack overflow.
# To avoid that, python has set maximum depth of 1000, if that is passed than
# recursion error wil be thrown

def recursion():
    recursion()

# It will give error as : RecursionError: maximum recursion depth exceeded
# recursion()

