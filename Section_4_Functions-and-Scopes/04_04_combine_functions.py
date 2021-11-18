# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting: str, name: str) -> str:
    """Generates a greeting"""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(greeting, name, text):
    def greet(greeting: str, name: str) -> str:
        """Generates a greeting"""
        sentence = f"{greeting}, {name}! How are you?"
        hail = sentence
        return hail
    hail = greet(greeting, name)
    letter = f"{hail},\n{text}\nThanks, {name}. Goodbye."
    return  print(letter)





name = input("Whom would you like to greet?\n")
greeting = input(f"How would you like to greet {name}?\n")
text = input(f"What would you like to say to {name}?\n")

write_letter(greeting, name, text)