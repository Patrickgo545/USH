"""
LAMBDA
------------

-Small single line functions that dont require you to state a def statement
-Used for quick one - time operations
"""

# 1. DOUBLE USING LAMBDA 
double = lambda x: x * 2

result = double(5)
print(result)



# 2. SORTING NAMES

# sorted()  -sort names based on length
# using lambda + len() to return names as their length for sorted

names = ['Alice', 'Bob', 'Charlie', 'Daisy' , 'Verylongnamedperson']
sorted_names = sorted(names, key=lambda name: len(name))

print(sorted_names)



# 3. FINDING EVEN NUMBERS

# filter()      -Filter out the even numbers from the list
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

# ODD NUMBERS

numbers1 = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x: x % 2 == 1 , numbers1))

print(odd_numbers)