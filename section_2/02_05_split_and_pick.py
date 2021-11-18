# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

# text = input("Give us a sentence, any sentence.\n   > ")
# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.


# test_text = "There was only one sort of person in our town, and that's the sort of person that you would never want to happen upon at night time."
# test_split_text = test_text.split()

text = input("Give us a sentence, any sentence.\n   > ")
split_text = text.split()


counter = 0
word_count = 0
d = {}
most_d = {}
most_count = 0
word_occurence = ''

for word in split_text:
    if word in d:
        count = d.get(word)
        word_count = count + 1          # builds og dictionary
        d.update({word:word_count})
    else:
        d.update({word:1})
for word in d:
    occ = d.get(word)                            
    if occ == most_count:     # use dictionary values here and conver the dictionary to a str at the end
        most_d.update({word:occ})
        most_count = occ
    elif occ > most_count:
        most_d.clear()
        most_d = {word:occ}
        most_count = occ

for word, occurence in most_d.items():
    word_occurence += f'{word} ({occurence})\n  '
    
most_print = f"\nMost commonly occuring word(s):\n  {word_occurence}"
print(most_print)


# print(d)
# print(most_d)
