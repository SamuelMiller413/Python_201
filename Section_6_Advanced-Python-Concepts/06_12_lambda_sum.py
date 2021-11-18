# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.




numbers = [4, 2, 3]
# def get_sum(x):
#     return sum(x)

# print(get_sum(numbers))

get_sum = lambda x: sum(x)
print(get_sum(numbers))

# the function would be:

# summation = sum(lambda x: x + x)
# print(summation)
# def square_root(x):
#     return x**2
# In the code snippet above, you defined a function, square_root() that takes an integer, x, as its argument and returns that number squared.

# You can write the same logic in a one-liner lambda expression:

# squared = lambda x: x**2