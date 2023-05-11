'''
COMPREHENSIONS

-Provide a concise & efficient way to create new sequences 
    Such as lists / dictionaries / & sets 
    Based on existing sequences 
'''

# 1. LIST COMPREHENSION

numbers = [1,2,3,4,5]
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)

# Addition
addition = [1,2,3,4,5]
addition_plus_one = [num + 1 for num in addition]

print(addition_plus_one)



    
# 2. DICTIONARY COMPREHENSION

# List of fruits
# len() specifies the length of the fruit name

fruits = ['apple' , 'banana' , 'cherry']
fruit_length = {fruit: len(fruit) for fruit in fruits}      #created a dictionary

print(fruit_length)                                         #List print: {'apple': 5 , ...}


# Create same list without a new dictionary 

fruits1 = ['apple' , 'banana' , 'cherry']
fruit_length1 = [len(fruit) for fruit in fruits]

print(fruit_length1)                                        #list print: [5,6,6]



# 3. SET COMPREHENSION

# Find all the unique numbers in a list
# {num for num in numbers}
    # num for num - what numbers are in the list

numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
unique_numbers = {num for num in numbers}

print(unique_numbers)