def titlecase(text):
    titlecase = []
    for word in text.split():
        cap_word = word.capitalize()
        titlecase.append(cap_word)
        
    return " ".join(titlecase)
user_input = input('Enter your sentence:  (type exit to close)\n    ')
while user_input.lower() != "exit":
    
    crash_blossom = titlecase(user_input)
    print(crash_blossom)
    user_input = input('Enter your sentence:  (type exit to close)\n    ')