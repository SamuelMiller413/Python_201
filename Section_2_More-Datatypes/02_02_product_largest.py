# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.


sordid_list = []
from resources import randlist
import math

for num in randlist:
    sordid_list.append(num)
sordid_list.sort()
print(f"List: {sordid_list}")
print(f"Largest Number: {sordid_list[-1]}")
print(f"Product of List: {math.prod(sordid_list)}")


# for num in list(randlist):
#     num_list.append(num)
#     sordid_list = num_list.sort()

# print(num_list)

# print(num_list.sort())

# print(sordid_numbers[-1])
# print(f"Largest Number: {sordid_numbers[-1]}")
