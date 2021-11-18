
   
# Write a script that sorts a list of tuples based on the number value in the tuple. For example:



unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

sordid_list = []
index = 0
flag = True

while flag == True:   # establish loop with simple boolean condition
    if len(sordid_list) == len(unsorted_list):
        break         # break loop once all tuples are accounted for in sorted loop
    else:
        index += 1    # tracking number to hold value against
        for element in unsorted_list :
            if element[1] == index:
                sordid_list.append(element)  
            else:
                continue
print(sordid_list)
