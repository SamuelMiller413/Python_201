# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

from pathlib import Path
all_words = []
reverse_words = ''
with open('words.txt', 'r') as fin:
    for word in fin.readlines():  
        word = word.rstrip()
        all_words.append(word)

all_words.reverse()

for word in all_words:
    reverse_words += f"\n{word}"

p = Path('words_reverse.txt')
p.write_text(reverse_words)
p.read_text()
test = p.read_text()
print(test)