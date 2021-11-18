# Write a script that locates your Desktop
# Fetches all files on it
# Counts files by type (use a dict to collect this data)
# print this file_dict to console

import csv
import pathlib
from typing import ContextManager
file_dict = {}

# Write a script that locates your Desktop
path_desktop = pathlib.Path("/Users/admin/Desktop")
# Fetches all files on it
# print(path_desktop)
for file in path_desktop.iterdir():
    file_name = file.name
    suff = file.suffix
    suff_count = 0
    
    # print(file_name)
    # Counts files by type (use a dict to collect this data)
    # +find way to log the suffix as a dict item, 
    # adding items to dict as it iterates
    if suff in file_dict:
        # print("flag")
        # if suff == '':
        #     count = file_dict.get(suff)
        #     suff_count = count + 1
        #     file_dict.update({'folder':suff_count})
        # else:
        count = file_dict.get(suff)
        suff_count = count + 1
        file_dict.update({suff:suff_count})
    
    else:
        file_dict.update({suff:1})

count = file_dict          # !!! 'count' variable is now the dictionary ('file_dict') you'll be using

print(count)

# with open("filecounts.txt", "r") as file_in:
#     print(file_in.read())


# with open("filecounts.csv", "a") as csvfile:
#     countwriter = csv.writer(csvfile)
#     data = [count[".code-workspace"], count[".csv"], count[".app"], count[""],  count[".png"], count[".jpg"], count[".py"]]
#     countwriter.writerow(data)




    

# print(count)






# >>>>>>   writing to file   <<<<<<<

# file_out = open("filecounts.txt", "w")     # write mode
# file_out = open("filecounts.txt", "a")     # 'append' mode
# file_out.write(str(count))
# file_out.write("\n")
# file_out.close()

# file_in = open("filecounts.txt", "r")
# contents = file_in.read()
# print(contents)
# list_of_contents = contents.split(" ")

# dict_of_contents = {}
# for x in range(0, len(list_of_contents), 2):
#     element = list_of_contents[x]
#     element_2 = list_of_contents[x + 1]    
#     dict_of_contents.update({element:element_2})
# print(dict_of_contents)

# ContextManager
# with open("filecounts.txt", "r") as file_in:
#     print(file_in.read())

# # csv file creation

# # -- snip --
# count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}
# with open("filecounts.csv", "a") as csvfile:
#     countwriter = csv.writer(csvfile)
#     data = [count[""], count[".csv"], count[".md"], count[".png"]]
#     countwriter.writerow(data)

# print(count)

# # _____>>>>>>  this following snippet is an exercise in scripting 
# # the functionality of the 'context manager' (with open...) 
# # and is not necessary going forward.
#         count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}
#         csvfile = open("filecounts.csv", "a")
#         count_string = '\n'
#         tracker = 0
#         for k, v in count.items():
#             tracker += 1
#             count_string += f"{str(v)}"
#             if tracker == len(count):
#                 break
#             else:
#                 count_string += ","     
#         csvfile.write(count_string)




# for i in range(0, len(sordid_list), 2):
#     element = sordid_list[i]
#     if (sordid_list.index(element) + 1) == len(sordid_list) and (len(sordid_list) % 2 != 0):
#         element_2 = 0
#     else:    
#         element_2 = sordid_list[i + 1]
#     my_tuple = (element, element_2)
#     tup_list.append(my_tuple)    
# print(tup_list)



# with open("filecounts.csv", "a") as csvfile:
#     countwriter = csv.writer(csvfile)
#     # data = [count[".code-workspace"], count[".csv"], count[".app"], count[""], count[".jpg"], count['.py'], count[".png"]]
#     data = []
#     # for k, v in count.items():
#     #     cap_header = ""            # this bliock is for creating headers but doesn't really work out -- saved just in case needed
#     #     if k == "":
#     #         cap_header = 'Folder'
#     #     for char in k:
#     #         if char == "'":
#     #             pass
#     #         elif char == ".":
#     #             pass
#     #         else:
#     #             cap_header += char.upper()
#     #     k_header = f"{cap_header}: {v}"
#     #     data.append(k_header)
#     countwriter.writerow(data)


# print(file_list)
# use "pprint" to display your output in a nice format