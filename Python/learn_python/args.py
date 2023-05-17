"""
*ARGS & *KWARGS
---------------

-Allows us to pass any number of arguments to a function
-Flexible functions that can work with different amounts of input
"""

# 1. COUNTING FRUITS

# Use len() to count the number of fruits & return the total count

def count_fruit(*fruits):
    return len(fruits)

total_fruits = count_fruit('apple', 'banana', 'orange', 'grape')
print('total fruits entered:' , total_fruits)



# 2. ADDING NUMBERS

#create a function that will let you add as many numbers as you'd like

def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = add_numbers(1,5,5,5,5,5,2,1,125)
print('sum of numbers:' , result)



# 3. GREETING FRIENDS

# create an *args function that will let you greet any number of friends

def greet_friends(*names):
    for name in names:
        print('Hello,' , name + '!')
        print('\n')

greet_friends('Pat' , 'Lillian' , 'Lucas' , 'Anthony')