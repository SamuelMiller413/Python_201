# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!


input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]
input_tuple = ()
tuple_list = []

for k, v in input_dict.items():
    item = k, v
    tuple_list.append(item)
my_results = sorted(tuple_list, key=lambda item:item[1])
if result_list == my_results:
    print(True)
else:
    print(False)


#     input_tuple += tuple(item)
# print(input_tuple)

# print(sorted(input_dict, key=lambda item:item[2]))



# input_tuple = tuple(input_dict[0])
# print(input_tuple)


# from operator import itemgetter, attrgetter

# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10), 
#     ]
# student_objects = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10), 
#     ]


# # print(sorted(student_tuples, key=lambda student: student[2]))   # sort by age
# # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
# print(sorted(student_objects, key=attrgetter('age')))