# Ask User to enter First or 2nd option
a = input("Enter 1 for Celsius to Fahrenheit OR Enter 2 for Fahrenheit to Celsius : ")

if(a == "1") :
    temp = float(input("Enter temperature in Celsius : "))
    fahrenheit = temp * 1.8 + 32;
    print("Fahrenheit : %0.2f" %fahrenheit)
elif (a == '2') :
    temp = float(input("Enter temperature in Fahrenheit : "))
    celsius = (temp - 32) * (5/9);
    print("Fahrenheit : %0.2f" %celsius)


