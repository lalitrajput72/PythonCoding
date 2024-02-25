var = 10

# ==================================
# If-else statement syntax in python
# ==================================

if var > 15:
    print("If statement")
else:
    print("else statement")

# Another syntax is elif which is usually else if in java

if var > 5:
    print("If statement")
elif var > 10:
    print("elif statement")
else:
    print("else statement")

# ==============================
# for statement syntax in python
# ==============================
cars = ['hyundai', 'suzuki', 'honda', 'Tata', 'Mahindra']

for i in cars:
    print(i, end=" ")
print()

# Loop over a string
lang = 'hindi'
for i in lang:
    print(i, end=" ")
print()

# range() funtion in Python : Works only on Integer
# takes max three parameter : start, end and step

for i in range(5):
    print(i, end=" ")
print()

for i in range(5, 10):
    print(i, end=" ")
print()

for i in range(10, 20, 3):
    print(i, end=" ")
print()

# ==============================
# while statement syntax in python
# ==============================
num = 2
while num < 5:
    print(num, end=" ")
    num = num+1
print()
# pass in python : It can be used as a placeholder of future code
# or we can use it to pass any iteration or call : No action will be performed when pass is executed

for i in range(10, 15):
    if(i < 12):
        pass
    else:
        print(i, end=" ")