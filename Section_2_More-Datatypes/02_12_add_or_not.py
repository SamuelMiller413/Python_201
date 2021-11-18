# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.



# Continuously collect number input from a user with a `while` loop.

zet = {'prime'}
lives = 5
points = 0

print(f"\nWelcome to the memory game!\nIn case you've forgotten, here are the rules:\n\
    You start with 5 lives and 0 points.\nWhen prompted, enter a number.\n  You earn a point if it's the first time you entered it.\n\
-but-\n  If you've already entered that number, you lose a life.\nLose all lives and lose the game,\nbut earn 10 points and win the game!")
while lives > 0 and points < 10:   
    x = input(f"\nEnter an integer:      (Points = {points} / Lives = {lives})\n  > ")
        # Confirm that the input can be converted to an integer,
    if x.isnumeric():
        if x in zet:    # If the element was already in the set, notify, deduct.
            lives -= 1
            print(f"\nUh oh! '{x}' has already been entered! You've lost a life23 :( only {points} left...")
        else:
            zet.add(x)
            points += 1
    else:
        print(f"\n'{x}' is not an integer.")
if lives == 0:
    print("\nYou ran out of lives. You lose.\n")
else:
    print("\nCongratulations, you're a winner!\n")
