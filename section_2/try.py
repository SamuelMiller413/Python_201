office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

big_set = set()
tup_1 = ()
string_ = ''
name = ''
big_list = []
list_to_print = []
dictio = {}
value_list = []
counter = 0 
trash_list = []
for el in office:
    name = el["full_name"] + " "
    item = el["item"] + " "
    name_split = name.split(" ")

    name__reversed = f"{name_split[1]}, {name_split[0]}"
    
    string_ = f"{name__reversed} {item}"
    list_of_string = string_.split(" ")
    big_list.append(list_of_string)

for i in big_list:
    string_2 = ' '
    for x in i:
        string_2 += x + ' '
    
    length = len(i[0])
    
    dictio[string_2] = length
for v in sorted( dictio.values() ):
    for key in dictio:
        if dictio[key] == v:
            if key in trash_list:
                pass
            else:
                print (key)
                trash_list.append(key) 
                break
# for k, v in dictio.items():
#     value_list.append(v)
# value_list.sort()
# print(value_list)
# # print(value_list)
# print(dictio)

# flag = True
# while flag == True:
#     if counter == len(dictio):
#         flag = False
#     for i in dictio:
#     # print(i)
#         if dictio[i] == counter:
#             print(i)
#             print(dictio[i])
#             dictio[i] = 5000
#             counter += 1
#         else:
#             counter+=1
#             print('flag_else')
# print(dictio)