# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.

def write_letter(name, text):
    letter = f"Hello {name},\n{text}\nThanks, {name}. Goodbye"
    return  print(letter)

name = "Jonathon"
text = "Don't forget to put the toilet seat back down when you're finished."
write_letter(name, text)
