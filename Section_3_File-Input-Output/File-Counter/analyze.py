# Use the `csv` module to read in and count the different file types.

import csv

with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["CODE-WORKSPACE", "CSV", "APP", "Folder", "PNG", "JPG", "PY"])
    counts= list(reader)

print(counts)
# # [{'CODE-WORKSPACE': '1', 'CSV': '1', 'APP': '1', 'Folder': '4', 'PNG': '18', 'JPG': '1', 'PY': '6'}]

# print((counts[0])['Folder'])
# print((counts[1])['PNG'])
# # CODE-WORKSPACE: 1,CSV: 1,APP: 1,Folder: 4,PNG: 18,JPG: 1,PY: 6