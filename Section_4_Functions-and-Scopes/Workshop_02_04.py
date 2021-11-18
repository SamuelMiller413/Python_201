
# >>>>>>>>>>>   Python 201 / Sections / 4) Functions And Scopes/ Introduction To Functions

# Functions are a fundamental concept in programming that touches on two important aspects:

# 1. Composition: 
# You use functions to break your code 
# into smaller chunks that 
# you can arrange and compose together.

# 2. DRY (Don't Repeat Yourself): 
# You write functions to compartmentalize and 
# generalize a sequence of instructions so that 
# you can use the same code for it in 
# multiple places in your script.

# basic function syntax:

# def my_func(parameter):
#     pass # Replace with code that does something
#     return  # Followed by a value that the function gives back

# Such a function definition consists of the following parts:

# 1. def keyword: tells Python that you're defining a function
# 2. Function name (e.g. my_func): a variable name used to refer to your new function object. The name should be descriptive of what the function does. You'll see examples of that later on.
# 3. Parameters: Optionally, a function can require some input, called a parameter. You specify which input is needed in the function definition.
# 4. Function body: your instructions that do something. In this example, you see a pass statement as a placeholder for the code you'll write here.
# 5. return statement: decides what will be the output of your function. A function can either return some value or None. If you don't specify a value, like in the example above, the function will return None.


# >>>>>>>>>>>   4) Functions And Scopes/ Example: Writing And Calling a Function_

# titlecase exercise:

# mock_input = "squad HELPS dog Bite VicTim"

# def titlecase(text):
#     titlecase = []
#     for word in text.split():
#         word = word.capitalize()
#         titlecase.append(word)
#         " ".join(titlecase)
#     return print(" ".join(titlecase))

# titlecase(mock_input)


# >>>>>>>>>>>   4) Functions And Scopes/ Familiar Functions

# Familiar Functions

# - print() is used to display output to the console. It takes a Python object as input and writes its string representation to your console. The print() function returns None.
# - type90 is used to find out the data type of an object. the obhect is the argument you pass to it, and the data type is the function's return value.
# - str(), int(), floart(), list(), etc. are functions that allow you to explicitly convert a value from one fata type to another. they take the value as their input, and return the converted value. 
#  - input() is used to collect user input through the CLI. The function takes a string as its input that will be used as a prompt for the user. It then collects the uiserr input and return s it as a string.
#  - open() allows you to create file objects that you can read from and write to. It takes a file path and a mofe as its input and returns a file object.

# - fruitful functions: return a vcalue that you want to use somewhere else
# - oid funtions: don't return a calue you defined, always return None in python. 
#     ex. "print()"
#         result = print("hello void!")
#         print(result)  # None

# FUNCTIONAL PROGRAMMING aims to to only use funtions that have no side-effects ("print('x') wheere 'x' is the side-effect") and always create the same output when given the same input.

# print = f'print = {print()}'
# string = f'string = {str()}'
# float = f'float = {float()}'
# integer = f'integer = {int()}'
# list = f'list = {list()}'
# # open = f'open = {open()}'
# input = f'input = {input()}'

# print(print)
# print(string)
# print(float)
# print(integer)
# print(list)
# print(input)
# # print(open)
# print(int())


# >>>>>>>>>>>   4) Functions And Scopes/ parts of a Function: The Header

# greeting function:

# def greet(greeting, name):
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

    # keyword: def 
    # name of funtion: greet
    # parameters and argument: (greeting, name)
        # parameters optional

        #    *$*    "A parameter is a variable in a function definition. 
            #   When a function is called, the arguments are the data that you pass 
            #   into the function's parameters."
    # option of : 'KEYWORD ARGUMENTS': greet(name="Martin", greeting="Hello")  # Call it with keywords
        # then they can be passed in any order
        # keyword arguments with default values:
            # def greet(greeting="Hi", name="User"):  # Adding defaults
            #     sentence = f"{greeting}, {name}! How are you?"
            #     return sentence

            # print(greet())
            # print(greet(name="Fievel" greeting="Hello"))

            # OUTPUT:
            # Hi, User! How are you?
            # Hello, Fievel! How are you?


# >>>>>>>>>>>   4) Functions And Scopes/ Parts Of A Function: The Body

# function body is what follows the ':'

# return statements make the function 'fruitful'
# void statement example: 
#     def void_func(message):
#         print(message)
# 'fruitful'example:
    # def fruitful_func(message):
    #     return message

        # Info: If you want to return more than one value from a function, 
        # then you need to wrap your data in a collection. 
        # Most of the time, you'll use tuples for this. 
        # For example, the built-in enumerate() function 
        # returns a tuple consisting of 
        # an index number and the element's value.


# >>>>>>>>>>>   4) Functions And Scopes/ Function Calls

# def greet(greeting, name):
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

# # print(greet("Hello", "World"))  # Hello, World! How are you?
# # print(greet("Howdy", "partner"))  # Howdy, partner! How are you?
# # print(greet("Zdravo", "prijatelj"))  # Zdravo, prijatelj! How are you?
# # print(greet("Hi", "Martin"))  # Hi, Martin! How are you? 

# # print(greet("Sah", "dih"))

# print(greet(42, 1011001))


# >>>>>>>>>>>   4) Functions And Scopes/ Args and Kwargs

# *args and **kwargs

#  - args stands for arguments
#  - kwargs stands for keyword arguments
    # The syntax that actually provides the functionality 
        # of this feature are the asterisks (* and **).

# The Single Asterisk (*):
#    If you add *args as a parameter to your function definition, 
#   it will package all passed arguments into a collection. 
#   You can then access each item like you would in a normal list.
#       More commonly, however, you'll just iterate over all items in args:

# def print_args(*args):
#     for a in args:
#         print(a)

# print_args("barcelona", "tahoe", "ubud", "koh tao")

# OUTPUT:
# barcelona
# tahoe
# ubud
# koh tao
        # -->  by prepending the parameter name with the single asterisk (*), 
            # you invoke the special language feature that allows you to pass 
            # as many arguments to your function call as you want to.

# The Double-Asterisk (**):
# Adding **kwargs to your function definition has a similar effect. 
# However, Python packages up your arguments in a 'mapping' instead.

# def print_kwargs(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
    
# print_kwargs(country='ukraine', city='odessa')

# OUTPUT:
# country ukraine
# city odessa

        # By prepending the parameter name with the double-asterisk (**), 
        #   you invoke the special language feature that allows you to pass 
        #   as many keyword arguments to your function call as you want to.

# Use Cases:

# def greet_many(greeting, *args):
#     greetings = ""
#     for name in args:
#         sentence = f"{greeting}, {name}! How are you?"
#         greetings += sentence + "\n"
#     return greetings

    # Info: Note that if you are mixing defined positional parameters, 
    # such as greeting, with *args, 
    #   then *args needs to come after 
    # any defined parameters in your function definition.

# print(greet_many('Hey there!', 'my friend', 'my lover', 'my associate', 'my partner'))

# using **kwargs instead:

# def greet_many(**kwargs):
#     greetings = ""
    
#     for greeting, name in kwargs.items():
#         sentence = f"{greeting}, {name}! How are you?"
#         greetings += sentence + "\n"
#     return greetings


# print(greet_many(mello='mary', hello='harry', gello='gary'))

# def make_pizza(*args):
#     for topping in args:
#         print(f"* {topping}")

# make_pizza('tomatoes') # collected in a tuple
# make_pizza('tomatoes', 'mushrooms', 'olives', 'garlic')

# def make_pizza(**kwargs): # collected in a dictionary
#     for k, v in kwargs.items():
#         print(f"{k} maps to {v}")
# make_pizza(dough='wheat', topping='tomato sauce', fire=True)


# >>>>>>>>>>>   4) Functions And Scopes/ Docstrings

# Special Comments:
#     Docstrings are special comments that describe functions, classes, and methods in Python

        # they should describe at least aspects of your function:
        #     1. what it does
        #     2. what arguments it takes
        #     3. what it returns

# Write a Docstring:
    # 2 essenbtial parts of a good docstring
        # 1. Use triple-double quotes (""") to begin and end a docstring.
        # 2. Write it starting at the first line of your function body

# def greet(greeting, name):
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence
#         # becomes
# def greet(greeting, name):
#     """Generates a greeting.

#     Args:
#         greeting (str): The greeting to use, e.g. "Hello"
#         name (str): The name of the person you want to greet

#     Returns:
#         str: A personalized greeting message
#     """
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

# Read a Docstring:

    # --> refer to 'docstring_thing.py'
# hotkey: ctrl+shift+2 or cmd+shift+2 


# >>>>>>>>>>>   4) Functions And Scopes/ Type Hinting

# def greet(greeting, name):
#     """Generates a greeting.

#     Args:
#         greeting (str): The greeting to use, e.g. "Hello"
#         name (str): The name of the person you want to greet

#     Returns:
#         str: A personalized greeting message
#     """
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

# Dynamic Typing And Static Typing:

    # Dynamic typing, also called "duck typing", evaluates variables and inputs at runtime of your script. There is no need to declare the type of a variable when you initialize it. Your variable, 
    # e.g. a, could be of any type, and change types throughout its lifetime:
# a = 3
# a = "hello"
# a = 4.2
# a = True

    # Static typing, on the other hand, gives every variable a specific type when you create it. In a statically-typed language, you can't change the variable's type once it's declared in the same way you can in Python.

# Type Hinting:

    # To add type hints to your function definition, you add the expected type of a parameter after a colon (:). You can also define the expected type of your return value with an arrow (->) at the end of the first line of your function definition:
    
#     example:
# def greet(greeting: str, name: str) -> str:
#     """Generates a greeting."""
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

            # Info: Python remains dynamically typed, 
            # which means that even if you add type hints 
            # to your function, the types aren't enforced.

# Enforced Type Hinting:
    # 'mypy' can be used to 'enforce static typing'
    # Info: mypy is an external package, which means you need to install it before you can use it. If you haven't done this before, read over the next sections about virtual environments and external packages before completing the exercise below.


# >>>>>>>>>>>   4) Functions And Scopes/ Introduction to Scopes

# Introduction to Scopes:

# Your greet() function contains three variables:

# 1. greeting
# 2. name
# 3. sentence

# greeting and name are two parameters that get filled with the value of the arguments a user passes when calling your function. sentence gets created within the body of your function.

# Local Function Scope:

# Function-internal variables live only inside the function. You can refer to the function parameters inside your function as much as you want to, but you won't be able to access them outside of it:

    # def greet(greeting: str, name: str) -> str:
    #     """Generates a greeting"""
    #     sentence = f"{greeting}, {name}! How are you?"
    #     return sentence
    # print(name)  # OUTPUT: NameError: name 'name' is not defined
    # print(sentence) <-- "squeeze"?  
    #                       # OUTPUT: NameError: name 'sentence' is 
    #                                   not defined

# Function-internal variables can't be re-used outside of the function's scope. To re-use any value generated in the function, you need to "squeeze" it through the return statement and expose it to your global scope.
# ---> "squeeze"

# >>>>>>>>>>>   4) Functions And Scopes/ Variable Scopes_ (video)

# following along::

# glob = 2
# print("glob" in globals())

# def fun():
#     loc = 2
#     print('glob' in locals())
#     print('loc' in locals())
#     print('loc' in globals())

# fun()

# glob = 2
# print("glob" in globals())

# def fun():
#     loc = 2
#     print(glob)
#     print('glob' in locals())
#     print('loc' in locals())
#     print('loc' in globals())

# fun()

# practical example:
# name = 'harry'
# print(name)
# def fun():
#     name2 = 'sally'
#     print(name)
#     print(name2)
# fun()
# print(name2)


# >>>>>>>>>>>   4) Functions And Scopes/ Variable Scopes

# How does Wikipedia define scope:

# In computer programming, the scope of a name binding – an association of a name to an entity, such as a variable – is the region of a computer program where the binding is valid: where the name can be used to refer to the entity. Such a region is referred to as a scope block. In other parts of the program the name may refer to a different entity (it may have a different binding), or to nothing at all (it may be unbound).

# scopes are like boxes within boxes

# 1. global scope
# 2. local scope

# name = "Mycroft"

# def print_name_box():
#     print(name)

#     def smaller_box():
#         print(name)

#         def smallest_box():
#             print(name)

#         smallest_box()

#     smaller_box()

# print_name_box()

# name = "Mycroft"

# def print_name_box():
#     print(name)

#     def smaller_box():
#         # (Re)assigning a variable within a local scope
#         # overwrites the same variable from an outer scope
#         # You also can't use the global variable *before*
#         # assigning it, if you assign it anywhere in that scope.

#         # --TASK--: uncomment the print() function below
#         #     and interpret the results when running the script

#         # print(name)
#         name = "Sherlock"

#         def smallest_box():
#             # Inner scopes always draw from the next-outer layer.
#             # After `name` got overwritten, the name that will
#             # be printed is NOT the global-scope name anymore
#             print(name)

#         smallest_box()

#     smaller_box()

# print_name_box()

# my_list = ["apple", "banana", "orange"]
# obj1 = enumerate(my_list)
# print(obj1)


# >>>>>>> LABS

# import random
# list_ = [1,2,3,4,5,5,6,7,8]

# ran = len(list_)
# x = random.randint(1, ran)

