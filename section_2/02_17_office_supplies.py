# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item




office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]


string_ = ''
name = ''
big_list = []
list_to_print = []
dictio = {}
trash_list = []

for el in office:
    name = el["full_name"] + " "
    item = el["item"]
    name_split = name.split(" ")

    name__reversed = f"{name_split[1]}, {name_split[0]}"
    # add formatting in here
    string_ = f"{name__reversed:<30}{item}"
    list_of_string = string_.split(" ")
    big_list.append(list_of_string)
    # print(item)
for i in big_list:
    string_2 = ''
    for x in i:
        string_2 += x + ' '
    
    length = len(i[0])
    
    dictio[string_2] = length
print('')

for v in sorted( dictio.values() ):
    for key in dictio:
        if dictio[key] == v:
            if key in trash_list:
                pass
            else:
                print(key)
                trash_list.append(key) 
                break
print('')
print('')
# string_ = ''
# name = ''
# big_list = []
# list_to_print = []
# dictio = {}
# value_list = []

# for el in office:
#     name = el["full_name"] + " "
#     item = el["item"] + " "
#     name_split = name.split(" ")

#     name__reversed = f"{name_split[1]}, {name_split[0]}"
    
#     string_ = f"{name__reversed} {item}"
#     list_of_string = string_.split(" ")
#     big_list.append(list_of_string)

# for i in big_list:
#     string_2 = ' '
#     for x in i:
#         string_2 += x + ' '
    
#     length = len(i[0])
    
#     dictio[string_2] = length

# for k, v in dictio.items():
#     value_list.append(v)
# value_list.sort()

# for v in value_list:
#     for key, value in dictio.items():
#         if value == v:
#             print(key)



# picking this up later:
# maybe i should sort all the names by length first, then loop over that list, 
# using each item as a key to call the associated value from the original dictionary??

# test = [{"full_name": "Jim Halpert", "item": "phone"}, {"full_name": "Toby Flenderson", "item": "files"}, {"full_name": "Michael Scott", "item": "world's best boss mug"}]



            
                

   
# print(dictio)
# # print(length)

# def return_key(val):
#     for key, value in dictio.items():
#         if value==val:
#             return key
    





# make dictionary k item v len
# for i in big_list:
#     sorted_list = sorted(big_list, key = len(i[0]))
#     list_to_print.append(sorted_list)
# print(list_to_print)


    # add to tuple?
# >>>>>>>>>>>>>>    by length of index 0 in string once formatted   <<<<<<<<<<<<<<<<<<
    
    
#     my_dict.update(item)    
# # print(my_dict)
# for k, v in my_dict:
#     string_1 += v
#     print(string_1)
    
    
    # name_split = my_dict["full_name"].split(" ")
    # name_split.reverse()
    # string_1 += str(name_split)
    # item = my_dict["item"]
    

# list(sorted(last_name, key = len))
# new_dict = {}
# for x in test:
#     # print(x)
#     my_dict = x
#     print('flag')
#     # print(my_dict['full_name'])
#     name_split = my_dict["full_name"].split(" ")
#     # print(name_split)
#     name_split.reverse()
#     # print(name_split)
#     new_dict.update({"full_name":name_split, "item":my_dict['item']})
#     # print(new_dict)

# key_access = len((new_dict["full_name"])[0])
# new_dict_list = new_dict
# print(new_dict_list)
# sorted_list = sorted(new_dict_list, key = key_access)
# print(sorted_list)

# # print(my_dict)





# name_list = []
# def convert(dictionary):
#     for x in dictionary:
#         my_dict = x
#         name = my_dict["full_name"].split(" ")
#         name_string = f"{name[1]}, {name[0]}"
#         item = my_dict["item"]
#         name_list.append(f'{name_string}           {item}')
#         list(sorted(name_list, key = len))
#         # name_list.sort(len(name[0]))
#         print(name_list)
#     # for y in name_list:
#     #     string_to_split = y
#     #     string_to_split.split(" ")
#     #     print(string_to_split[0])
#         # name_list.split(" ")
#         # print(name_list[0]) #sort this list by last name length


        

# convert(office)

# # else:
# #             name_string = f"{name[2]}, {name[0]} {name[1]}"

# # for name_count in name[1]:
# #             name_length = len(name_count)
# #             name_list.append(name_length)
# #             if len(name) == 2:
# #                 name_string = f"{name[1]}, {name[0]}"