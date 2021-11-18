# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

flattened_list = []
starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    
for x in starter_list:
    alchemy = x
    for y in alchemy:
        flattened_list.append(y)
    
print(flattened_list)

# tuple_list = tuple(starter_list)
# print(tuple_list)
# flattened_list = list[tuple_list]
# print(flattened_list)