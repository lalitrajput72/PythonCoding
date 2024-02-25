# We can have list of mixed datatypes as well in python

student = [5, 3.5, 'Harry', 9, 10]
print(student)

# Get list element by index
print(student[2])

# Add elements in python list
student.append("Mark")
print(student)

# Update a list
# Unlike Python tuples, lists are mutable, and we can change the element of a list
student[3] = 15
print(student)

# Remove an element from a list, provide the item value instead of index to remove the item from list
student.remove(15)
print(student)

# Check list length
print(len(student))

# Iterate through a list in python
for i in student:
    print(i, end=":")
print()
# you cannot use sort() if list has different types of data type values
# Check if an item is present in a list or not

print('Mark' in student)
print('Bark' in student)
