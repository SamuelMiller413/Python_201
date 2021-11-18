# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

randlist.sort()
sordid_list = randlist
# test_even = [6, 14, 18, 27, 30, 43, 43, 47, 48, 59, 64, 89, 94, 98]
# test_odd = [6, 14, 18, 27, 30, 43, 43, 47, 48, 59, 64, 89, 94]
tup_list = []

for i in range(0, len(sordid_list), 2):
    element = sordid_list[i]
    if (sordid_list.index(element) + 1) == len(sordid_list) and (len(sordid_list) % 2 != 0):
        element_2 = 0
    else:    
        element_2 = sordid_list[i + 1]
    my_tuple = (element, element_2)
    tup_list.append(my_tuple)    
print(tup_list)

