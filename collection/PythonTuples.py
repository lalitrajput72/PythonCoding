# The difference between Pyhton Tuples and Python List is
# List are mutables
# Tuples are immutable
# List created using [] and tuples created using ()

animalTuple = ('Cat', 'Dog', 5)
for i in animalTuple:
    print(i)

# Update an item from tuple
# It will give you error-> TypeError: 'tuple' object does not support item assignment

#  animalTuple[2] = 10
