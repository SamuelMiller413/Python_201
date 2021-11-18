# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.


import csv
import pathlib
from pathlib import Path
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

# with open("filecounts.txt", "r") as file_in:
#     print(file_in.read())
data_path = Path("/Users/admin/Desktop")            # this enables the script to work from anywhere on any system
with open(data_path.joinpath("filecounts.csv"), "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[".code-workspace"], count[".csv"], count[".app"], count[""],  count[".png"], count[".jpg"], count[".py"]]
    countwriter.writerow(data)