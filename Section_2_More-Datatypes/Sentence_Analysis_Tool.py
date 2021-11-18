# Sentence Analysis Tool
# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

# Note: ignore all spaces.

# Example input:

# I love to work with dictionaries!
# Example output:

# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28


# >>>>>><<<<<< Reverse Engineered >>>>>>><<<<<<<

import string

sentence = "I love to work with dictionaries!"
my_dict = {"Upper Case: ": 0, "Lower Case: ": 0, "Punctuation: ": 0, "Total Chars: ": 0}
for char in sentence:
    if char.isupper():
        my_dict['Upper Case: '] += 1
        my_dict['Total Chars: '] += 1
    if char.islower():
        my_dict['Lower Case: '] += 1
        my_dict['Total Chars: '] += 1
    if char in string.punctuation:
        my_dict['Punctuation: '] += 1
        my_dict['Total Chars: '] += 1
    
    
for k, v in my_dict.items():
    print(k, v)




# ------->  Notes for reference:

# key: "greeting"
# value: "hello"

# my_dict = {"greeting": "hello", "name": "martin" }

# users = {"mary": 22, "caroline": 99, "harry": 24}