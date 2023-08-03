# 133 Introduction & Program Requirements for the Higher Lower Game

# 1. Break the problem down 
# 2. Create a to do list 
# 3. Turn the problem into comments 
# 4. Write code, run code, fix code



# To dos

# 1. Greet the user 
import higherlower_art
print(higherlower_art.logo)


# 2. Give the user two random choices, label the choices A and B
import random
from higherlower_gamedata import data
## generate a random number between 0 and the length of the list with follower count -1
r1 = random.randint(0, len(data)-1)
r2 = random.randint(0, len(data)-1)
A = data[r1]
B = data[r2]
print(f"Compare A: {A['name']}, {A['description']} from {A['country']}")
print(higherlower_art.vs)
print(f"Against B: {B['name']}, {B['description']} from {B['country']}")


# 3. The user selects one s/he thinks has more followers
user_input = input('Who do you think has more followers? Type "A" or "B":')
# 3a. Assign user_input to relevant variables
if user_input == 'A':
    user_input = A
else:
    user_input = B

# 4. If the user is correct, make the user's guess the new A
avg = (A['follower_count'] + B['follower_count'])/2
score = 0
if user_input['follower_count'] > avg:
    score += 1
    print(f"You're right. Your score is {score}")
    A = user_input
# 4a. What happens when the user's guess is wrong?
elif user_input['follower_count'] == avg:
    score += 1
    print(f"Both actually have the same number of followers. Your score is {score}")
    A = user_input
else:
    print(f"Sorry. That's wrong. Final score: {score}")


# 5. Generate another random choice, label it B 
r2 = random.randint(0, len(data)-1)
B = data[r2]
# this will go inside the if block, if the user's guess is right

# 6. Continue until the user guesses wrong
continue_game = True
while continue_game = True:
if
elif
else:
    continue_game = False


# 6. Keep tally of the right guesses, that is the user's score
line 42


# 7. If the user guesses wrong, print sth like you lose and your score is this 
line 51


# 8. Play again?
if input('Do you want to play again? Type y or n: ') == 'y':
    # something







# 134 Solution & Walkthrough of the Higher Lower Game

# Now compile 

import higherlower_art
print(higherlower_art.logo)

import random
from higherlower_gamedata import data
## generate a random number between 0 and the length of the list with follower count -1
r1 = random.randint(0, len(data)-1)
r2 = random.randint(0, len(data)-1)
# What if both r1 and r2 are same?
while r1 == r2:
    r2 = random.randint(0, len(data)-1)
A = data[r1]
B = data[r2]

score = 0
continue_game = True
while continue_game == True:
    print(f"Compare A: {A['name']}, {A['description']} from {A['country']}")
    print(higherlower_art.vs)
    print(f"Against B: {B['name']}, {B['description']} from {B['country']}")
    # What if the user types lowercase A/B?
    user_input = input('Who do you think has more followers? Type "A" or "B":').upper()
    if user_input == 'A':
        user_input = A
    else:
        user_input = B

    avg = (A['follower_count'] + B['follower_count'])/2
    if user_input['follower_count'] > avg:
        score += 1
        print(f"You're right. Your score is {score}")
        A = user_input
        r2 = random.randint(0, len(data)-1)
        B = data[r2]
        # What if A and B is the same random account?
        while A == B:
            r2 = random.randint(0, len(data)-1)
            B = data[r2]
    elif user_input['follower_count'] == avg:
        score += 1
        print(f"Both actually have the same number of followers. Your score is {score}")
        A = user_input
        r2 = random.randint(0, len(data)-1)
        B = data[r2]
        # What if A and B is the same random account?
        while A == B:
            r2 = random.randint(0, len(data)-1)
            B = data[r2]
    else:
        print(f"Sorry. That's wrong. Final score: {score}")
        continue_game = False
        if input('Do you want to play again? Type y or n: ') == 'y':
            continue_game = True




# 135 Study Tip_ Set Reminders in Your Calendar to Review

