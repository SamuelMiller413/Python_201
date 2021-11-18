# # >>>>>> Python 201/ Sections/ 2) More Datatypes/ Tuples Are Immutable

# # 1. Create a for loop and iterate over one of your tuples. Print out each element.
# conc_tup = ()
# tup1 = ("Mr.", 77, "has", "arrived")
# print(tup1)
# for element in tup1:
#     conc_tup += (element,)
# print(conc_tup)

# # 2. Create a tuple that is a collection of only str elements. 
# #   Access the second letter of the second element in your tuple using indexing.
# tup2 = "Mr.", "smith", "goes", "to", "washington's", "grave."
# # print(tup2)
# # print(str(tup2[1])[1])

# # 3. Iterate over your tuple full of strings and print out the last letter of each string only. 
# #   For this, you'll need to combine iteration and indexing.

# for word in tup2:
#     print(str(word)[-1])

#  >>>>>>>>>>> Python 201 / Sections / 2) More Datatypes / Hello Lists
# # Square Brackets
# list1 = [1, 42, "hello"]
# print(list1)  # OUTPUT: [1, 42, "hello"]

# # List Function
# tup = (1, 42, "hello")
# list2 = list(tup)
# print(list2)  # OUTPUT: [1, 42, "hello"]

# bucket_list = ["climb Mt. Everest", "eat fruits from a tree"]

# print(bucket_list[0])  # OUTPUT: "climb Mt. Everest"


# # Access the last element in a list using negative indexing.
# print(bucket_list[-1])

# Create longer bucket list with at least six items. 
#   Then use slicing and steps to pick out only every second element in the list. 
#       Don't use a loop for this!
#  note: using indexing and stride instead?

# bucket_list_2 = ["learn to code", "raise kids", "publish a full length book", "learn neuroscience", "eat fruit from a tree I've planted", "live in central america"]

# print(bucket_list_2[1::2])

# >>>>>>>>>  2) More Datatypes / About Python Lists_
#       video-follow-along

# a, b, c = "lists", "tuples", "dictionaries"



# datatypes = ['lists', "tuples", "dictionaries", 2, 3.0, ['hei there', []]]

# datatypes.pop()

# print(datatypes[0])

# datatypes = datatypes[0:2]
# print(datatypes)

# datatypes.append("dictioanries")
# print(datatypes)

# >>>>>>>>>  2) More Datatypes / Lists Are Mutable

# bucket_list[1] += " that I planted"
# print(bucket_list)

# #  alias-ing: 2 references to the same object
# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)  # True
# print(a is b)  # False

# b = a
# print(a == b)  # True
# print(a is b)  # True

# b[0] = 4
# print(a)  # OUTPUT: [4, 2, 3]

# >>>>>>>>>  2) More Datatypes / List Methods

# bucket_list = ["climb Mt. Everest", "eat fruits from a tree that I planted"]

# Add an element # list.append()
# bucket_list.append("sail across the Atlantic ocean")  # OUTPUT: ["climb Mt. Everest", "eat fruits from a tree that I planted", "sail across the Atlantic ocean"]
# print(bucket_list)
# Remove an element # list.pop()
# bucket_list.pop()
# print(bucket_list) # OUTPUT: ["climb Mt. Everest", "eat fruits from a tree that I planted"]

# next_task = bucket_list.pop()

# print(next_task)
# print(bucket_list)

# list.remove()
# bucket_list.remove("climb Mt. Everest")
#  - or -
# bucket_list.remove(bucket_list[0])

# a = [1, 2, 3, 2]
# a.remove(a[3])
# print(a)

# list.insert()
# bucket_list.insert(1, "sail across the Atlantic Ocean")

# list.sort()
# a = [3, 0, 999, 42]
# a.sort()

# using operators
# list_1 = 1
# list_2 = 2
# list_3 = 1, 2

# list_add = list_1 + list_2
# # list_minus = list_3 - 1
# list_mult = list_2 * list_2
# list_div = list_1 / list_2

# # print(list_3 + list_3 + list_1)

# # list_1 and list_2 aren't lists!

# List Methods:
# list.append(item)
# list.pop()
# list.remove(item)
# list.insert(index, item)
# list.sort()
# # >>>>>>>>>  2) More Datatypes / list Comprehensions

# names = ["Ada", "Bertha", "Carol"]
# lowercase_names = [x.lower() for x in names]

#  list comprehensions are only one-liner shortcuts for for loops in Python. 
# Anything you can do with a list comprehension, you can also do with a for loop. 
# It just takes you a couple more lines of code:

# names = ["Ada", "Bertha", "Carol"]

# lowercase_names = []
# for x in names:
#     lowercase_names.append(x.lower())

# print(lowercase_names)  # OUTPUT: ['ada', 'bertha', 'carol']

# joke = "red"
# joke.append("x").remove("d")

# # turn a comprehension into a for loop
# nums = [1, 2, 3, 4, 5, 6]
# print([sum(nums[i:i+3]) for i in range(0, len(nums),3)])
# list_1 = []
# for i in range(0, len(nums), 3):
#     list_1.append([sum(nums[i:i+3])])
# print(list_1)

# >>>>>>>>>  2) More Datatypes / Wow, Such List Comprehensions_

# weather = ['rainy', 'cloudy', 'sunny', 'snowy']

# doge_weather = []
# for w in weather:
#     dw = f"such {w}"
#     doge_weather.append(dw)

# print(doge_weather)

# doge_weather = [f"such {w}, wow" for w in weather if not w == 'rainy']
# print(doge_weather)
# doge_weather = [w.upper() for w in weather if not w == 'rainy']
# print(doge_weather)



# >>>>>>>>>  2) More Datatypes / Hello Sets

# s1 = {1, 2, 3}  # OUTPUT: {1, 2, 3}
# s2 = set([1, 2, 3])  # OUTPUT: {1, 2, 3}
# s3 = set()  # OUTPUT: {}

# url_list = ['http://www.example.com', 'http://www.setsareuseful.com', 'http://www.example.com']
# unique_urls = set(url_list)
# print(unique_urls) # OUTPUT: {'http://www.example.com', 'http://www.setsareuseful.com'}

# a = {45, 68, 23, 1, 34, 23, 1, 24}
# print(a)
# b = {56, 67, 12, 23, 35, 12, 78}
# print(b)
# c = a
# print(c)
# d = b
# print(d)
# e = c.union(d)
# print(e)
# f = c.update(d)
# print(f)

# s = set()
# s1 = {2, 3, 4}
# # d = {} This creates a "dictionary"
# # s1[0] Cannot Index a set!

# s2 = s1 | {3, 4, 5}

# for i in s2:
#     print(i)

# s_long = {2, 4, 6, 8, 1, 5, 9, 11, 34}
# # for i in s_long:
# #     print(i)

# s1 = {1, 2, 3}
# s1 | s_long
# print(s_long)



# >>>>>>>>>  2) More Datatypes / Hello Dictionaries

# Creating A Dictionary
# You can create a dictionary using curly braces ({}) 
# and adding keys and values that are separated by a colon (:). 
# Multiple entries are separated by commas (,), just like elements in collections:

# my_dict = {"greeting": "hello", "name": "martin"}

# The dictionary my_dict has two items in it:

# "greeting": "hello"
# "name": "martin"
# Each of these two items consists of a key and a value. 
# If you take apart the first element, then you'll see that it consists of:

# key: "greeting"
# value: "hello"

# my_dict = {"greeting": "hello", "name": "martin" }

# users = {"mary": 22, "caroline": 99, "harry": 24}
# print(users["mary"])

# # change
# users['harry'] = 20
# print(users['harry'])

# # add
# users['ludvik'] = 9
# print(users)
# print(users['ludvik'])
#         # If you're using the syntax to change the value 
#         # of a key that doesn't exist yet, 
#         # it gets added as a new entry to your dictionary.

# # remove
# # ( method: dict.pop(key) )
# users.pop('harry')
#     # -or-  ( with keyword: del ) ->if you're certain that the key is in the dictionary:  
# del users['harry]'
#         # to remove a key regardless of whether you know it's in the dictionary:
#     del users['harry', None]



# >>>>>>>>>  2) More Datatypes / About Python Dictionaries (video)
        
        # follow along:

# >>> my_dict = {}
# >>> my_dict
# {}
# >>> type(my_dict)
# <type 'dict'>
# >>> 
# >>> my_dict["greeting"] = "hei!"
# >>> my_dict
# {'greeting': 'hei!'}
# >>> my_dict["greeting"]
# 'hei!'
# >>> my_dict['greeting'] = "hello."
# >>> my_dict['greeting']
# 'hello.'
# >>> my_dict[[2, 2]] = 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'
# >>> 
# >>> my_dict[(2, 2)] = 2
# >>> my_dict
# {'greeting': 'hello.', (2, 2): 2}
# >>> my_dict[(1, "hei")] = [2, "ho
#   File "<stdin>", line 1
#     my_dict[(1, "hei")] = [2, "ho
#                                 ^
# SyntaxError: EOL while scanning string literal
# >>> my_dict[(1, "hei")] = [2, "ho"]
# >>> my_dict
# {(1, 'hei'): [2, 'ho'], 'greeting': 'hello.', (2, 2): 2}



# >>>>>>>>>  2) More Datatypes / Dictionary Mappings

# users = {'mary': 22, 'caroline': 99, 'harry':20}

# ( method: dict.items() )
# for user, age in users.items():
#     print(user, age)

#  # printing keys:
# for k in users:
#     print(k)
#     # - or - ( method: dict.keys() )
# for k in users.keys():
#     print(k) 

# ( method: dict.values() )
# for v in users.values():
#     print(v)


# # Change the age of "caroline" from 99 to 26.

# users['caroline'] = 26
# for user, age in users.items():
#     print(user, age)

# # to empty the dictionary ( method: dict.clear() )
# users = {'mary': 22, 'caroline': 99, 'harry': 20}
# users.clear()  # OUTPUT: {}

# 

# other methods:
# dict.get(key[default])
#     Return the value for key if key is in the dictionary, else default. 
#     If default is not given, it defaults to None, so that this method never raises a KeyError.
# dict.pop(key[default])
#     If key is in the dictionary, remove it and return its value, else return default.
#     If default is not given and key is not in the dictionary, a KeyError is raised.
        # Example:
        # random sales dictionary
        # sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

        # element = sales.pop('apple')

        # print('The popped element is:', element)
        # print('The dictionary is:', sales)
# dict.update(key[default])
    # Update the dictionary with the key/value pairs from other, 
    # overwriting existing keys. Return None.
    # update() accepts either another dictionary object or an iterable of key/value pairs 
    # (as tuples or other iterables of length two). 
    # If keyword arguments are specified, 
    # the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).






# >>>>>>>>>  2) More Datatypes / Recap Datatypes

# int: Integer numbers, such as 12
# float: Floating-point numbers, such as 42.0
# str: Text data, consisting of collections of characters, such as "hello"
# tuple: Immutable, ordered collections of any type, such as ("age", 33)
# list: Mutable, ordered collections, of any type, such as [1, 2, 4, 8]
# set: Unordered collections of unique items, such as {"hello", "world", 42}
# dict: Mutable mappings between keys and values, such as {"name": "feivel", "age": 2}