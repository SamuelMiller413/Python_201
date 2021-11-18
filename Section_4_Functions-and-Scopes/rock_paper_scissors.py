import random
import time


hand_dict = {1:'Rock', 2:'Paper', 3:'Scissors'}

def get_hand(hand):
    # 1 = rock, 2 = paper, 3 = scissor 
    # print(f"computer number number = {number}")
    # print(f"you"
    if hand not in range(1,4):
        result = "fail"
    elif hand == 1:
        if number == 1:
            result = 't'
        if number == 2:
            result = 'l'
        if number == 3:
            result = 'w'
    elif hand == 2:
        if number == 2:
            result = ''
        if number == 3:
            result = 'l'
        if number == 1:
            result = 'w'
    elif hand == 3:
        if number == 3:
            result = 't'
        if number == 1:
            result = 'l'
        if number == 2:
            result = 'w'
    return result
def determine_winner(result):
    if result == 't':
        determination = f"\nYou: {hand_dict[user_hand]},\nMe: {computer_hand}\n    Tie!\n"
    elif result == 'l':
        determination = f"\nYou: {hand_dict[user_hand]},\nMe: {computer_hand}\n    You Lose!\n"
    elif result == 'w':
        determination = f"\nWell would you look at that,\nYou: {hand_dict[user_hand]},\nMe: {computer_hand}\n   YOU WIN!!\n"
    elif result == 'fail':
        determination = f"\nWhoops that's not a valid answer! You lose! By I showed {computer_hand}...\n"
    return determination 
         
message = "\n\
It's time for Rock, Paper, Scissors!\n\
    1 = Rock\n\
        2 = Paper\n\
            3 = Scissors"
print(message)
time.sleep(.5)

message = "I, the computer, will be your opponent."
print(message)
time.sleep(.5)

user_hand = int(input("So what'll it be then, eh? Show us your hand!\n    ->  "))
number = random.randint(1,3)
computer_hand = hand_dict[number]
determinator = get_hand(user_hand)
time.sleep(.25)

print(determine_winner(determinator))


# user_hand = int(input("So what'll it be then, eh? Show us your hand!\n    ->  "))
# print(hand_dict[user_hand])

