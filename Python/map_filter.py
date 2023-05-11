"""
MAP & FILTER
---------------

-Perform operations on Iterables like lists & tuples

-map()      Used for applying a lambda function to each element in a iterable
-filter()   Used for selecting elements based on a condition (defined by lambda)
"""

# 1. MAPPING NUMBERS TO THEIR SQUARES

# map() function creates a new iterator with the squared values

numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x ** 2 , numbers))

print(squared_numbers)



# 2. FILTER EVEN NUMBERS

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0 , numbers))

print(even_numbers)



# 3. CONVERTING TEMPERATURES

temperatures = [25,30,15,20,35]
converted_temperatures = list(map(lambda x: (x * 9/5) + 32, temperatures))

print('temperatures in C' , temperatures)
print('temperatures from C to F:' , converted_temperatures)