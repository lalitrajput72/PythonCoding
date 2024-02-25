# Ask user to provide the three sides

a = float(input("Enter the first side : "))
b = float(input("Enter the Second side : "))
c = float(input("Enter the Third side : "))

semiParameter = (a+b+c)/2

print("Semi-perimeter of the trianlge is : {0}". format(semiParameter))

area = (semiParameter * (semiParameter-a) * (semiParameter-b) * (semiParameter-c)) ** 0.5
print("Area of the trianlge is : %0.2f" %area)