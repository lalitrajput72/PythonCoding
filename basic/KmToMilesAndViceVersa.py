# Ask User to enter First or 2nd option
a = input("Enter 1 for Km to miles OR Enter 2 for Miles to Km : ")

if(a == "1") :
    temp = float(input("Enter distance in Km : "))
    miles = temp * 0.621371
    print("Miles : %0.2f" %miles)
elif (a == '2') :
    temp = float(input("Enter distance in Miles : "))
    km = temp * 1.609344
    print("Km : %0.2f" %km)


