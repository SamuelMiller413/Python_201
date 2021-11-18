# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

word_list = []
long_word_list = []
with open('words.txt', 'r') as fin:
    for word in fin.readlines():  
        word = word.rstrip()
        word_list.append(word)

for w in word_list:
    if len(w) > 20:
        long_word_list.append(w)
        print(w)
    else:
        pass
