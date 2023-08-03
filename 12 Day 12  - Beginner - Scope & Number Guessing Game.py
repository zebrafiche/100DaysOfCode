# 115 Namespaces_ Local vs. Global Scope

# Scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# enemies inside function: 2
# enemies outside function: 1

# Local Scope

# Exists within functions
def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
print(potion_strength)

# 2
# NameError: name 'potion_strength' is not defined

# variables created only inside the function cannot be accessed outside the function 

# Global Scope
player_health = 10
def drink_potion():
  potion_strength = 2
  print(player_health)
  print(potion_strength)
drink_potion()

# 10
# 2

# Global variables are available within functions, no matter how deep it gets nested 

# This concept doesn't only apply to variables
# It also applies to functions and basically anything you name 
# This concept is called Namespace

player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
        print(potion_strength)

drink_potion()

# NameError: name 'drink_potion' is not defined
# You can call the function drink_potion() in local scope now, since it was named locally 




# 116 Does Python Have Block Scope_

# If you create a new variable inside local scope this is okay
# It will work inside the local scope

game_level = 3
enemies = ['Skeleton', 'Zombies', 'Alien']
if game_level < 5:
   new_enemy = enemies[0]
print(new_enemy)

# Skeleton

# But in our potion_strength example we could not do it, right?
# The thing to remember here is that this Namescope concept is applicable for functions only
# If the block is an if block, while loop, for loop etc. then it does not count as creating a local scope




# 117 How to Modify a Global Variable

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# enemies inside function: 2
# enemies outside function: 1

# It is not good practice to give both your local and global variable the same name 

# So how to we change the value of the global variable enemy?

enemies = 1

def increase_enemies():
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# UnboundLocalError: local variable 'enemies' referenced before assignment

# Python wants us to define the variable locally before trying to modify it 


# To change it, we have to say that we have a global variable somewhere outside the function 
# And that we want to change that global variable

enemies = 1

def increase_enemies():
  global enemies
#   without mentioning that we are referencing to enemies the global variable, we cannot change it 
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Why so hard?
# Because you won't be doing it very often
# And there is a significant chance that when you do your global variable will be somewhere inside huge lines of codes
# This makes you prone to making errors, thus you have to declare global enemies
# Because the function will be called multiple times when the code gets executed
# And everytime the global variable will change
# Not suggested


# Instead do this

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# enemies inside function: 1
# enemies outside function: 2




# 118 Python Constants and Global Scope

# You should in fact use global scopes when you are defining constants
# Constants that you never plan on changing

pi = 3.14159

# So to distinguish the constants (i.e. variables that you are never going to change)
# to variables (i.e. variables subject to change)
# The naming convention is to turn it all uppercase

PI = 3.14159
REDDIT_HANDLE = _therafi




# 119 Introducing the Final Project_ The Number Guessing Game

from guessthenumber_art import logo
print(logo)
import random
lowerlimit = random.randint(1, 1000)
upperlimit = lowerlimit + 200
number = random.randint(lowerlimit, upperlimit)

def assess():
   global guess
   global number
   if guess > number:
      print('Too high')
      guess = int(input('Guess again: '))
   elif guess < number:
      print('Too low')
      guess = int(input('Guess again: '))
   elif guess == number:
      print('You got it, good')


print('Welcome to the number guessing game')
print(f"I am thinking of a number between {lowerlimit} and {upperlimit}")
print(f"Psst, the number is {number}")

mode = input("Choose difficulty. Type 'easy' or 'hard': ")

difficulty = {
   "hard": 5,
   "easy": 10,
   }

print(f"You chose {mode} difficulty, you get {difficulty[mode]} guesses")
guess = int(input('Go ahead, guess the number: '))
no_guesses = 1

while guess != number and no_guesses < difficulty[mode]:
  assess()
  no_guesses += 1
  print(f"You have {difficulty[mode]-no_guesses} guess(es) left")
  
  
if guess == number:
   print('You win')
else:
   print('You ran out of guesses. You Lose')



# 120 Solution & Walkthrough to the Number Guessing Game

game = True
while game == True:
  # from guessthenumber_art import logo
  # print(logo)
  import random
  lowerlimit = random.randint(1, 1000)
  upperlimit = lowerlimit + 200
  number = random.randint(lowerlimit, upperlimit)

  def assess():
    global guess
    global number
    if guess > number:
        print('Too high')
        guess = int(input('Guess again: '))
    elif guess < number:
        print('Too low')
        guess = int(input('Guess again: '))
    elif guess == number:
        print('You got it, good')


  print('Welcome to the number guessing game')
  print(f"I am thinking of a number between {lowerlimit} and {upperlimit}")
  print(f"Psst, the number is {number}")

  mode = input("Choose difficulty. Type 'easy' or 'hard': ")

  difficulty = {
    "hard": 5,
    "easy": 10,
    }

  print(f"You chose {mode} difficulty, you get {difficulty[mode]} guesses")
  guess = int(input('Go ahead, guess the number: '))
  no_guesses = 1
  print(f"You have {difficulty[mode]-no_guesses} guess(es) left")

  while guess != number and no_guesses < difficulty[mode]:
    assess()
    no_guesses += 1
    print(f"You have {difficulty[mode]-no_guesses} guess(es) left")
    
    
  if guess == number:
    print('You win')
  else:
    print('You ran out of guesses. You Lose')

  if input("Play Again? Type 'y' or 'n': ") == 'n':
    game = False



# 121 Don't be too hard on yourself

