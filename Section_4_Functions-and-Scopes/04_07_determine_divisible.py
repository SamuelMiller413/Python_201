# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages
# ==================================================================

# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
def or_div_check(num):
    if (num % 4) == 0 or (num % 7) == 0:
        return True
    else:
        return False # boolean

# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
def and_div_check(num):
    if (num % 4) == 0 and (num % 7) == 0:
        return True
    else:
        return False # boolean

# - take in a number from the user between 1 and 1,000,000,000
number = input("Enter Number between 1 and 1,000,000,000\n  ")
forward = False
while forward == False:
    if number.isdigit():
        number = int(number)
        if number in range(1, 1000000001):
            forward = True
        else:
            number = input("Your answer doesn't fit the parameters. Try again\n  ")
    else:
        number = input("Your answer doesn't fit the parameters. Try again\n  ")
    
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 

new_variable_1 = or_div_check(number)
new_variable_2 = and_div_check(number)

# - print your the result variables with descriptive messages
def response(variable):
    if variable is True:
        analysis = 'divisible'
    else:
        analysis = 'not divisble'
    return analysis

or_analysis = response(new_variable_1)
and_analysis = response(new_variable_2)

# print(f"Your number ({number}) {or_analysis} by 4 or 7, and it is {and_analysis} by both.")

if new_variable_1 and new_variable_2 == True:
    print(f"Your number ({number}) {or_analysis} by 4 or 7, and it is {and_analysis} by both.")
elif new_variable_1 == True:
    if new_variable_2 == False:
        print(f"Your number ({number}) {or_analysis} by 4 or 7, but not by both.")


# Without Comments:

# def or_div_check(num):
#     if (num % 4) == 0 or (num % 7) == 0:
#         return True
#     else:
#         return False # boolean

# def and_div_check(num):
#     if (num % 4) == 0 and (num % 7) == 0:
#         return True
#     else:
#         return False # boolean

# def response(variable):
#     if variable is True:
#         analysis = 'divisible'
#     else:
#         analysis = 'not divisble'
#     return analysis

# number = input("Enter Number between 1 and 1,000,000,000\n  ")
# forward = False
# while forward == False:
#     if number.isdigit():
#         number = int(number)
#         if number in range(1, 1000000001):
#             forward = True
#         else:
#             number = input("Your answer doesn't fit the parameters. Try again\n  ")
#     else:
#         number = input("Your answer doesn't fit the parameters. Try again\n  ")

# new_variable_1 = or_div_check(number)
# new_variable_2 = and_div_check(number)
# or_analysis = response(new_variable_1)
# and_analysis = response(new_variable_2)

# # if new_variable_1 and new_variable_2 == True:
#     print(f"Your number ({number}) {or_analysis} by 4 or 7, and it is {and_analysis} by both.")
# elif new_variable_1 == True:
#     if new_variable_2 == False:
#         print(f"Your number ({number}) {or_analysis} by 4 or 7, but not by both.")