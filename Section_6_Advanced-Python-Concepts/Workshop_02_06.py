# >>>>>>>>>>>>>>   6) Advanced Python Concepts / Different Ways Of Importing Code

# Diferent Ways of Impoting Code:

# given the file structure of:
#     codingnomads
#         L_ ingredients.py
#         L_ soup.py

#     you can get access to anything defined in ingredients.py with an import statement:
#         #soup.py
#         from ingredients import carrot
        
#         print(carrot)


# Namespace Preservation:

# sometimesd it's helpful to keep clear the origin of where some code is defined. shorten it as:

#     import ingredients
    
#     print(ingredients.carrot)

# this calls variables or functions defined in ingredients.py through the 'ingredients.' 'namespace'


# Alias Imports:

# you may want to preserve the namespace but not type so much.
#     so you can assign an 'alias' to your code module:
    
#         #soup.py
#         import ingredients as i

#         print(i.carrot)
                
#                 L> 'i' is the alias for the namespace

# some times namespaces are assigned aliases by default:
#     import pandas as pd
#     import numby as np




# >>>>>>>>>>>>>>   6) Advanced Python Concepts / Nested NameSpaces

# Nested Namesapaces:

# importing code which is nestedd in additional folders:

#     codingnomads
#     |-----ingredients.py 
#     |-----recipes.py 
#     |       L__soup.py 
#     L-----cook.py

#         How can you access the logic you wrote in soup.py from your cook.py script?


# Deeper Namespaces:

# #cook.py
# import ingredients as i
# import recipes.soup as s

# c = i.carrot
# s.make_soup(c)
#     python treats the addintional folder as an extra namespace

#         Note: For the code snippet to work, 
#         you need to have both a carrot variable defined 
#         in ingredients.py, as well as a make_soup() function
#         in recipes/soup.py that takes one argument. 
#         You can only import and use what you've actually defined.




# >>>>>>>>>>>>>>   6) Advanced Python Concepts / Unexpected messages

# Unepected Messages:


# if this:
# # ingredients.py
# def prepare(ingredient):
#     return f"cooked {ingredient}"

# carrot = "carrot"
# salt = "salt"
# potato = "potato"

# print(prepare(potato))  # <-----what if you've kept this print statement becasue you were testing things while writing the script?



# Side effects from importing:

# when in soup.py and importing carrot:
#     # soup.py
#     from ingredients import carrot

    # output:
    #     somehow you get a potato in there!

    #     Info: When you import code from a module, 
    #     you execute the whole script. 
    #     If there's any code execution written in the script, 
    #     it'll run and potentially produce some unexpected output.




# >>>>>>>>>>>>>>   6) Advanced Python Concepts / Dunder Name


# To avoid code execution in your source module during import, you can do two things:

# 1. Remove any code execution from the file and make sure it only defines functions, 
# classes, and variables without doing anything else.
# 2. Use the __name__ namespace and nest your code execution there.


# Dunder Name:

# To avoid executing code during imports, 
# but leaving it in the original module file, 
# you can add the following code to the bottom of your module:

# if __name__ == "__main__":
#     # your code execution goes here

#     L__>  if you run this program directly 
#             instead of importing it as a module, 
#             o the following:

# By adding if __name__ == "__main__:" to the bottom of your script, and indenting any code execution below it, you achieve the following:

# Running the module directly executes the nested code logic
# Importing the module in another file skips that code logic



# >>>>>>>>>>>>>>   6) Advanced Python Concepts / Comprehensions,,,Anonymous Functions



# >>>>>>>>>>>>>>   6) Advanced Python Concepts / Expressions and Statements


# Expressions:

# Expressions are a combination of programming logic that evaluates to a result. For example, adding two numbers together is an expression because it results in the sum of the two numbers:

# 2 + 3  # OUTPUT: 5
# In the code snippet above, you can see that 2 + 3 has a result, 5. When you execute the expression 2 + 3, you'll hold a value in your digital hand. This makes 2 + 3 an expression.


# Statements:
# Statements are a more general term for all sorts of pieces that make up your code. In programming, statements are the building blocks that constitute a program.

# 'x = 2' is a statement


# Expressions and statements in a program:
# x = 2 + 3
# If you pick this short code snippet apart, you'll see that while the complete line of code is a statement, it also contains an expression:

# Expression: On the right side of the statement, there is an expression, 2 + 3, that evaluates to the integer 5.
# Statement: The statement x = expression saves the value of the expression 2 + 3 in the variable x.


# why??:

# One example of where the distinction between statements and 
# expressions is important is when passing arguments to functions. 
# You can pass an expression as an argument to a function, 
# but you can't pass a statement as an argument.


# Recap
# As a rule-of-thumb, you can remember that expressions evaluate to a result and statements don't.


# word = "CodingNomads"
# k = [c for c in word if c not in "aeiou"]
# print(k)


# Write a script that sorts a list of tuples based on the number value in the tuple. For example:

# My solution:

# unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
# sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]
# sordid_list = []
# counter = 0
# flag = True
# while flag == True:
#     if len(sordid_list) == len(unsorted_list):
#         break
    
#     else:
#         counter += 1
#         for element in unsorted_list :
#             if element[1] == counter:
#                 sordid_list.append(element)
               
#             else:
#                 continue
# print(sordid_list)

# lambda solution:
# sorted_list = sorted(unsorted_list, key=lambda x: x[1])
# print(sorted_list)

# function solution;
# def get_order(tup):
#     return tup[1]
# sorted_list = sorted(unsorted_list, key=get_order)
# print(sorted_list)    


# example = [('b', 2), ('a', 1), ('c', 3)]
# print(example[0])