# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word. <- +letter?? oh wait it is the word...
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

text = ''
test_text = 'hello world'
result_list = list()
str_word = ''


for char in test_text:
    if char.isalpha():
        str_word += char
    else:
        tup_word = tuple(str_word)
        result_list.append(tup_word)
        tup_word = ''
        str_word = ''
            
tup_word = tuple(str_word)
result_list.append(tup_word)
print(result_list)

# the supple tuple was my repl pupil