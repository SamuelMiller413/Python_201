# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"
sp = ""
t = tuple(string)
tp = ""
for char in string:
    # print(char)
    sp += char + "."
print(sp)

for element in t:
    # print(element)
    tp += element + "."
print(tp)



