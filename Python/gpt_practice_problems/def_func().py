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


