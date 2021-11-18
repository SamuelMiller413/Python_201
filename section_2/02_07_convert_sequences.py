# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
tuple_string = tuple(string)
print(tuple_string)
list_tuple = list(tuple_string)
print(list_tuple)
list_tuple[0] = 'k'
print(list_tuple)
tuple_list = tuple(list_tuple)
print(tuple_list)