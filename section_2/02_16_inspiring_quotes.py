# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]
# list[dict[str, str]]

# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname
        # "quote" - Last, first

# print(f'"{famous_quotes[0].values("full_name")}" - {famous_quotes[0].values("quotes")}')

def convert(dictionary):
    for item in dictionary:
        my_dict = item
        name = my_dict["full_name"].split(" ")
        if len(name) == 2:
            name_string = f"{name[1]}, {name[0]}"
        else:
            name_string = f"{name[2]}, {name[0]} {name[1]}"
        quote = my_dict["quote"]
        print(f'"{quote}" - {name_string}')

convert(famous_quotes)
# test_1 = [{"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."}]
# test_2 = [{"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy is about telescopes."}]
# convert(test_1)
# convert(test_2)

# print(name)
# print(name_reverse)
