# Write a lambda function that does not take in an arguments 
# but returns a value. Print the return value.

# print(list(map(lambda x: x + 1, range(20))))
get_5 = lambda: 5
behold_the_void = lambda: 'void'
print(behold_the_void())
print(get_5()) 
# list(map(lambda x: x**2, range(10)))