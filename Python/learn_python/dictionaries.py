'''
DICTIONARIES 
------------

- Advantage of using Dictionaries & keys
    Very fast, so you can assume its updating in real time

    Can be used to check if something is in the dictionary
    print('key' in x)   # Does x have "key value" within it?    
        Return: True or False

'''

# 1. Accessing dictionary values

dictionary_x = {'key': 4}
value = dictionary_x['key']

print('The value associated with "key" is' , value)



dictionary_y = {'dictionary_y': [1,2,3,4]}
value_y = dictionary_y['dictionary_y']

print(dictionary_y)


# 2. Adding & Modifying Dictionary Entries

y = {'key_y': 4}
y['new_key'] = 7    # adding new key value pair
y['key_y'] = 10     # Modifying the value of an existing key

print(y)