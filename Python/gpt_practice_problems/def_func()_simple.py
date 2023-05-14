# SIMPLER PROBLEMS FROM GPT

'''
AREA OF A RECTANGLE
Write a function called calculate_rectangle_area that takes the length and width 
of a rectangle as parameters and returns the area of the rectangle. 
The formula to calculate the area of a rectangle is length * width.'''

# 1. AREA OF A RECTANGLE 

l = int(input('Length: '))
w = int(input('Width: '))

def calculate_rectangle_area(l , w):
    area = l * w
    return area

result_area = calculate_rectangle_area(l,w)
print(result_area)



'''
Write a function called greet_user that takes a user's name as a parameter and returns a greeting message. 
The function should add the user's name to a greeting message, such as "Hello, [name]! Welcome!" and return the resulting message.'''

# 2. GREETING MESSAGE

name = input('What is your name? ')

def greet_user(name):
    print('Hello!' , name , 'welcome!')

greet_user(name)



'''Write a function called find_maximum that takes two numbers as parameters and returns the maximum of the two numbers. 
You can use conditional statements (if-else) to compare the numbers and determine the maximum.'''

# 3. MAXIMUM OF 2 NUMBERS

print('Enter 2 numbers: I will tell you which one is larger')

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

def find_maximum(x , y):
    if x == y:
        print('x equals y')
    
    elif x > y:
        print(x , 'is greater than' , y)
    
    else:
        print(y , 'is greater than' , x)

find_maximum(x , y)



'''
Write a function called calculate_sum that takes a list of numbers as a parameter and returns the 
sum of all the numbers in the list. You can use a loop to iterate through the list and keep track of the running sum.'''

# 4. SUM OF A LIST

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1,2,3,4,5]

result = calculate_sum(numbers)
print(result)