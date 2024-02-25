# A set is a collection of unique data, meaning that elements within a set cannot be duplicated.
# Note: The set has no particular order.

# [] for list
# () for Tuples
# {} for set

number = {4, 5, 3, 7 ,8}
print(number)

# Put duplicate values in set, it will give you unique element back only in any order
number = {4, 5, 3, 7 ,8, 8, 4, 7}
print(number)

empty_set = set()
empty_dictionary = {}

# sets are mutables but since they doesn't have any order so indexing here is not possible
number.add(10)
print(number)

# remove element from set
number.discard(5)
print(number)

# Union in set
a = {1,2,3,4}
b = {5,6,7,8}

print("Union of a and b :", a | b)
# OR
print("Union of a and b : ", a.union(b))

# Intersection
print("Intersection of a and b :", a & b)
# OR
print("Intersection of a and b : ", a.intersection(b))

