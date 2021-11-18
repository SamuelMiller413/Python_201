# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.


import time
middle = []
flag = True

def make_sandwich(middle): # we might need '*args here
    """
    Makes a Sandwich
    Args:   
        - takes an arbitrary amount of toppings
    Returns:
        Sandwich: formatted string representing a sandwich with the bread on top and bottom,
        and the toppings in between. 
    """ 
    ingredients = ''
    for item in middle:
        ingredients += f"{item:^30}\n"
    slice = f'====={bread}====='
    return  f'Okay! Here it is:\n\n{slice:^30}\n{ingredients}{slice:^30}\n'

bread = input(f"\nLet's make a sandwich! What would you like to use for bread?\n  ")
ingredient = input(f"\nGreat idea! What would you like to put in the sandwich?\n   ")
middle.append(ingredient)
while flag == True:
    ingredient = input(f"\nAlright. What else would you like to put in the sandwich?    (or say 'when')\n   ")
    if ingredient.lower() == 'when':
        flag = False
    else:
        middle.append(ingredient)
middle = tuple(middle)
sandwich = make_sandwich(middle)

print('Alright. Hold on now while I make it')
time.sleep(.75)
print('.')
time.sleep(.75)
print(' * makes sandwich * ')
time.sleep(2)
print(sandwich)

