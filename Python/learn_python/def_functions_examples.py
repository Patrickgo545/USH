'''
FUNCTIONS
-------------
'''
#x = int(input('x: ' ))
# = int(input('y: '))

def add_numbers(x,y):
    return x + y

print(add_numbers(2,2))


# 1. Double
num = int(input('double: '))

def double(num):
    return num * 2

print(double(num))


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


# 3. NUMBER SQUARED

#define function 
def square(num):
    return num ** 2 
# Create variable for result
x = int(input('Square: '))
result = square(x)

print('the square of', x , 'is' , result)



# 4. Adding numbers

def addition(a , b):
    return a + b

x = int(input('lets add two numbers, list the first number '))
y = int(input('Whats the second number? '))

result = addition(x , y)
print('result: ' , result)



# Greeting function

def greet():
    print('whats good?? ;)')

greet()