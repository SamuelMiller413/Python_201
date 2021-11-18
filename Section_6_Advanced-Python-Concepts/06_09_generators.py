# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.
demo_list = [1, 2, 3, 4, 5]
generator = (x + 1 for x in demo_list)
print(generator)
print(type(generator))
for i in generator:
    print(i)