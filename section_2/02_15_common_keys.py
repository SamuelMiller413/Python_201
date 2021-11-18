# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:


dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
result = {"a": 3, "b": 2, "c": 7 , "d": 2}
result_ = {}

for key, value in dict_1.items():
    if key in result_:
        result_[key] += value
    else:
        result_[key] = value
for key, value in dict_2.items():
    if key in result_:
        result_[key] += value
    else:
        result_[key] = value

if result_ == result:
    print(True)
else:
    print(False)