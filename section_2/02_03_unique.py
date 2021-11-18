# Write code that creates a list of all 
# unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list_ = [1, 45, 23, 'Mr.', 13, 13, 1, 78, 23]
unique_list = []
d = {}
for i in list_:
    if i in unique_list:
        unique_list.remove(i)
    else:
        unique_list.append(i)
print(unique_list)

    