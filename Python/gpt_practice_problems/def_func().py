'''
Practice Problem 1: Calculate Average
Write a function called calculate_average that takes in a list of numbers as a parameter 
and returns the average of those numbers. The function should calculate the sum of the numbers 
and then divide it by the total count of numbers.'''

# 1. CALCULATE AVERAGE


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    
    total = sum(numbers)
    average = total / len(numbers)

    return average

numbers = [1,2,3,4,5,6,7]

test = calculate_average(numbers)
print(test)



'''
Write a function called is_palindrome that takes in a string as a parameter and returns True if 
the string is a palindrome and False otherwise. A palindrome is a word or phrase that reads the same forwards 
and backwards, ignoring spaces and punctuation. The function should ignore case sensitivity as well.'''

# 2. CHECK PALINDROME

word = input('Enter a word & i\'\ll check if its a palindrome: ')

def is_palindrome(word):
    if word == word[::-1]:
        return True

    else:
        return False

test_palindrome = is_palindrome(word)
print('Palindrome: ' , test_palindrome)



'''
Write a function called calculate_factorial that takes an integer as a parameter and returns the factorial of that number. 
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. For example, 
the factorial of 5 (denoted as 5!) is 5 x 4 x 3 x 2 x 1, which equals 120.'''

# 3. CALCULATE FACTORIAL

number = 5

def calculate_factorial(x):
    factorial = x
    i = x
    while i > 1:
        factorial *= (i - 1)
        i -= 1
        return factorial
    
result = calculate_factorial(number)
print(result)



'''
Write a function called count_vowels that takes a string as a parameter and returns the count of vowels (a, e, i, o, u) in that string. 
The function should be case-insensitive, meaning it should count both uppercase and lowercase vowels.'''

def count_vowels():
    no