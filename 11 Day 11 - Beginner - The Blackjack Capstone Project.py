# 107 Day 11 Goals_ what we will make by the end of the day.en_US

# Blackjack game by the end of the day



# 108 Blackjack Program Requirements and Game Rules

# The mechanics of the game
# Blackjack is also known as 21
# Add up your cards to the largest number without going over 21
# More than 21 is called a bust, you lose
# All the cards 2 - 10 count as their face value 
# Jack, Queen and King count as 10
# Ace as one or eleven, you can decide which to make a win
# If the dealer's sum add up to less than 17, they must take another card 
# The Joker card has no function or standing in the game Blackjack

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# we assume that we are gonna have an infinite deck
# in reality they are limited, when a card is drawn, there is less probability of it being redrawn
# we want each card has equal chance of occuring, that is why infinite deck


from blackjackart import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def choose_cards(a):
    a.append(random.choice(cards))
def sum_list(b):
    x = 0
    for i in b:
        x += i
    return x
def decision():
    for key in game_dict:
        if game_dict[key] > 21:
            print(f"{key} went over and lost")
            
game_dict = {'You': 0, 'Computer': 0}

print(logo)
start = True 
while start:
    input("Do you want to play a game of blackjack? type 'y' or 'no': ")
    choices = []
    comp_choices = []
    choose_cards(choices)
    choose_cards(choices)
    choose_cards(comp_choices)
    game_dict['You'] = sum_list(choices)
    game_dict['Computer'] = sum_list(comp_choices)
    print(f"Your cards: {choices}, current score: {game_dict['You']}")
    print(f"Computer's first card: {comp_choices}")

    game = True
    while game and game_dict['You'] < 21 and game_dict['Computer'] < 21:
        continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
        if continue_game == 'y':
            choose_cards(choices)
            choose_cards(comp_choices)
            game_dict['You'] = sum_list(choices)
            game_dict['Computer'] = sum_list(comp_choices)
            print(f"Your cards: {choices}, current score: {game_dict['You']}")
            print(f"Computer's final hand: {comp_choices}, final score: {game_dict['Computer']} ")
        elif continue_game == 'n':
            game = False

    winningscore = 0
    for player in game_dict:
        if game_dict[player] > 21:
            print(f"{player} went over and lost")
        elif game_dict[player] > winningscore:
            winningscore = game_dict[player]
            print(f"{player} won with a score of {winningscore}")

    if input('Want to play again?: ') == 'n':
        start = False

        



# 109 Hint 4 & 5 Solution Walkthrough

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

# deal the computer and the user both two cards each
# made a mistake here
user_cards = []
computer_cards = []
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())






# 110 Hint 6-8 Solution Walkthrough

# create a function to calculate score, you can look up the sum() function 
# the sum function takes a list and gives a total of all items in the list 

# Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
# 0 will represent a blackjack in our game.

# Inside calc_score() check for an 11 (ace). 
# If the score is already over 21, remove the 11 and replace it with a 1. 
# You might need to look up append() and remove()

def calc_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards,append(1)
    return sum(cards)




# 111 Hint 9 Solution Walkthrough_ Refactoring and calling calculate_score()

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

user_cards = []
computer_cards = []
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calc_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards,append(1)
    return sum(cards)

user_score = calc_score(user_cards)
computer_score = calc_score(computer_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

# Both computer and the user will be dealt two cards. The computer will only reveal one, as the rules of blackjack

is_game_over = False
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True




# 112 Hint 10-12 Solution Walkthrough

#Hint 10: If the game has not ended, ask the user if they want to draw another card. 
#If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. 
#The computer should keep drawing cards as long as it has a score less than 17.

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

user_cards = []
computer_cards = []
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calc_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards,append(1)
    return sum(cards)

is_game_over = False

while not is_game_over:

    user_score = calc_score(user_cards)
    computer_score = calc_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")


    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calc_score(computer_cards)




# 113 Hint 13 Solution Walkthrough


# Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. 
# If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
# If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. 
# If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

user_cards = []
computer_cards = []
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calc_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards,append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return 'Lose, Opponent has Blackjack'
    elif user_score == 0:
        return 'Win with a Blackjack'
    elif user_score > 21:
        return 'You went over. You lose'
    elif computer_score > 21:
        return 'Opponent went over. You win'
    elif user_score > computer_score:
        return 'You win'
    else:
        'You Lose'  

def play_game():
    is_game_over = False

    while not is_game_over:

        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    print(f"Your final hand: {user_cards}, and final score: {user_score}")
    print(f"Computer's final hand: {computer_score}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? type 'y' or 'no': ") =='y':
    play_game()




# 114 A Solid Foundation goes a Long Way