# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.


all_words = []
short_words = []
long_words = []
with open('words.txt', 'r') as fin:
    for word in fin.readlines():  
        word = word.rstrip()
        all_words.append(word)

low_bar = 30
short_list = []
long_list = []
high_bar = 1

for w in all_words:
    wl = len(w)
    if wl <= low_bar:
        if wl < low_bar:
            short_list = [w]
            low_bar = wl
        else:
            short_list.append(w)
    if wl >= high_bar:
        if wl > high_bar:
            long_list = [w]
            high_bar = wl
        else:
            long_list.append(w)

print(short_list)            
print(long_list)
print(len(all_words))
    
