# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# 1.
set_list = set(list_)
print(f"1. {set_list}")

# 2.
list_2 = []
for i in list_:
    if i in list_2:
        continue
    else:
        list_2.append(i)
print(f'2. {list_2}')