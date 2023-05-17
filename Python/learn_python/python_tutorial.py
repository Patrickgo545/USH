'''
DATATYPES
------------------- 
'''

# Boolean 
True #1 
False #0



'''
PRINT & OUTPUTS
------------------- 
'''
print('Hello' , 'test' , 100 , end='\n')

print('New line')
print('\n')



'''
VARIABLES
------------------- 
'''
# Naming conventions

# Cannot start with a number 
# Snake Case
hello_world = 'test1'



'''
USER INPUT
------------------- 
'''
prompt = input('enter string here: ')
prompt_number = int(input('enter number: '))

prompt_return = prompt , prompt_number

print(prompt_return)
print('\n')



'''
ARITHMETIC OPERATOR
------------------- 

- Python follows basic order of operations

/ - Divisor operator always returns a float
// - Divisor: Return to int
% - Returns the remainder after the division
** - Raise to the power of

'''

operator_examples = '+ , - , * , /' 



'''
STRING METHODS
-------------------

-Affects strings
-Can chain string methods together

-Basic methods
    .upper() - Uppercase entire string
    .lower() - Lowercase entire string
    .capitalize() - Capitalize first letter in string
    .count(...) - count how many instances of what's within the parenthesis
'''

string_upper = 'uppercase'
print(string_upper.upper())

string_lower = 'LOWERcAsE'
print(string_lower.lower())

string_capitalize = 'capitalize'
print(string_capitalize.capitalize())

string_hello = 'HeLLo world'
print('count all instances of "LL":' , 
      string_hello.count('LL'))

#Chaining string methods
print('chaining method - count all instances of "ll":' , 
      string_hello.lower().count('ll'))

print('\n')



'''
CONDITIONAL OPERATORS
---------------------

==  Equal to
!=  Not equal to
<=  Less than or Equal to
>=  Greater than or equal to
<   Less than 
>   Greater than

'''



'''
CHAINED CONDITIONALS
--------------------

-testing if statement is TRUE
-returns boolean 
-order of operations 
    not | and | or

and
or 
not - will flip true & false statements
'''

result = 'result1' or 'result2' 
# if either are true then 'result' = TRUE



'''
IF | ELSE | ELIF
----------------

-else   must come after if
-elif   must come after if 
'''

example = input('Name: ')
if example == 'pat':
    print('handsome')

else: 
    print('okay')

#elif
example2 = input('Number: ')
if example2 == 10:
    print('you typed 10')

elif example2 < 10:
    print('less than 10')

elif example2 > 10: 
    print('greater than 10')
    


'''
LIST | TOUPLES 
---------------

[]  Brackets create a list

-list position starts at 0

LIST FUNCTIONS
    len(<list>)
        tells us the length of the list

    x.append('hello')
        appends hello to the end of the list 

    x.extend([1,2,3,4,5,5,])
        appends this list to the end of list x

    x.pop()
        remove the last element of the list & returns the list
    x.pop(0)
        remove the first element of the list & returns the list 

TOUPLES
()  Parenthesis create Touples

-immutable lists
    cant be changed or appended

-can chain lists & touples 
'''
x_list = [0 , 1 , 2 , 'three']

print(len(x_list))

x_list.append(4)
print(x_list)

x_list.extend([5,6,7])
print(x_list)

x_list.pop(0)
print(x_list)

print('\n')



'''
FOR LOOP 
-------------

-iterate a set number of times
-different from while
    while doesnt have a determined set of times

i   iterator or counter variable
in  keyword we always have 

range() function, created a collection of numbers we give it
    (start, stop, step)

    if you only do 1 number it will assume you're starting at 0 & stepping by 1

'''

for i in range(10):
    print(i)

print('\n')
for i in range(2 , 10):
    print(i)

print('\n')
for i in range(2 , 11 , 2):
    print(i)



'''
WHILE LOOPS
------------

while condition == true:
    execute will continue to run as long as condition remains true

'''

i = 0
while i < 10:
    print('run')
    i +=1

# Break loop structure

i = 0
while True:
    print('run1')
    i += 1 
    
    if i ==10:
        break
                                            


'''
SLICE OPERATOR
--------------

-take a slice of a list / string / touple 

sliced = x[start:stop:step]
'''

x = [0,1,2,3,4,5,6,7,8]
y = ['hi' , 'hello' , 'goodbye' , 'cya' , 'sure']
s = "hello"

sliced = x[0 : 4 : 2]
print(sliced)

sliced1 = x[:4]
print(sliced1)

sliced2 = x[::-1]
print(sliced2)

sliced3 = x[4:1:-1]
print(sliced3)

# can slice a string
sliced_string = s[:3:1]
print(sliced_string)



'''
SETS
-----------

-use this operator to find out if something exists or doesnt in a large list
'''

x = set()
s = {4,32,2,2}
s2 = {3,4,22,1}

print(s.union(s2))


'''
DICTS
-----------
'''



'''
COMPREHENSIONS
-----------------
'''



'''
FUNCTIONS
-------------
'''
#x = int(input('x: ' ))
# = int(input('y: '))

def add_numbers(x,y):
    return x + y

print(add_numbers(2,2))


'''# 1. Double
num = int(input('double: '))

def double(num):
    return num * 2

print(double(num))
'''

# 2. Is prime
prime = int(input('is this num prime? '))

def is_prime(prime):
    if prime <= 1:
        return False
    for i in range(2 , int(prime ** .5)+1):
        if prime % i == 0:
            return False
    return True

print(is_prime)