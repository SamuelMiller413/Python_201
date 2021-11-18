# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

import csv
import pathlib
from typing import ContextManager
file_dict = {}


path_desktop = pathlib.Path("/Users/admin/Desktop")

for file in path_desktop.iterdir():
    file_name = file.name
    suff = file.suffix
    suff_count = 0
    
    if suff in file_dict:
        count = file_dict.get(suff)
        suff_count = count + 1
        file_dict.update({suff:suff_count})
    
    else:
        file_dict.update({suff:1})

count = file_dict          # !!! 'count' variable is now the dictionary ('file_dict') you'll be using
# print(count)
# with open("filecounts.txt", "r") as file_in:
#     print(file_in.read())
# test_count = {'.png': 14, '.code-workspace': 1, '.csv': 2, '.app': 1, '': 4, '.jpg': 1, '.py': 6, '.docx': 1, '.txt': 1}
data_dict = {}
data = []
field_names = []
for k, v in count.items():
        cap_header = ""           
        if k == "":
            cap_header = 'Folder'
        for char in k:
            if char == "'":
                pass
            elif char == ".":
                pass
            else:
                cap_header += char.upper()
        k_header = {cap_header:v}
        # data_dict.update(k_header)
        data.append(count[k])
        field_names.append(cap_header)
        
print('flag')

# for k, v in data_dict.items

with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    countwriter.writerow(data)


with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=field_names)
    counts= list(reader)


print(counts)