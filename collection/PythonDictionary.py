# A Python dictionary is a collection of items that allows us to store data in key: value pairs.

country_capitals_dictionary = {
    "India" : "Delhi",
    "US" : "Washington",
    "Australia" : "Canabara"
}

print(country_capitals_dictionary)

# Dictionary keys are immutable

# valid dictionary
# integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}

# valid dictionary
# tuple as a key
my_dict = {(1, 2): "one two", 3: "three"}

# invalid dictionary, TypeError: unhashable type: 'list'
# Error: using a list as a key is not allowed
# my_dict = {1: "Hello", [1, 2]: "Hello Hi"}

# valid dictionary
# string as a key, list as a value
my_dict = {"USA": ["Chicago", "California", "New York"]}

# The keys of a dictionary must be unique.
# If there are duplicate keys, the later value of the key overwrites the previous value.

car_model_dictionary = {
    "Hyundai" : 2020,
    "Suzuki" : 2016,
    "Honda" : 2024,
    "Suzuki" : 2024
}
print(car_model_dictionary)

# Access dictionary item simply by giving key
print(car_model_dictionary["Honda"])
print(car_model_dictionary["Hyundai"])
#Note: We can also use the get() method to access dictionary items.
print(car_model_dictionary.get("Suzuki"))
# Add items to a dictionary
car_model_dictionary["Mercedes"] = 2026
print(car_model_dictionary)

# Update
car_model_dictionary["Mercedes"] = 2027
print(car_model_dictionary)
# Remove item from dictionary
del car_model_dictionary["Mercedes"]
print(car_model_dictionary)

# Note: We can also use the pop() method to remove an item from a dictionary.

# If we need to remove all items from a dictionary at once, we can use the clear() method.
# clear the dictionary
#car_model_dictionary.clear()
print(car_model_dictionary)

# Iterate over dictionary
for car in car_model_dictionary:
    # Print key
    print(car, end=" ")
    # Print values
    print(car_model_dictionary[car])

print(len(car_model_dictionary))


