# Add type annotations to the three functions shown below.

def multiply(num1: int, num2: int) -> int:
    return num1 * num2
# Original
# def multiply(num1, num2):
    # return num1 * num2

def greet(greeting: str, name: str) -> str:
    sentence = f"{greeting}, {name}! How are you?"
    return sentence
# Original
# def greet(greeting, name):
#     sentence = f"{greeting}, {name}! How are you?"
#     return sentence

def shopping_list(*args: tuple) -> tuple:
    [print(f"* {item}") for item in args]
    return args
# original (tuple of one that is a list)
# def shopping_list(*args):
#     [print(f"* {item}") for item in args]
#     return args

