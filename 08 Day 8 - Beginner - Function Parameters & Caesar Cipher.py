# 079 Day 8 Goals_ what we will make by the end of the day

# By the end of the day we will have built a caeser cipher

# To do this, we will learn about 
# Functions and Inputs
# Arguments and Parameters




# 080 Functions with Inputs

def my_function():
    print('Hello')
    print('How are you?')

my_function()
# Hello
# How are you?

# Fucntions with inputs

def my_function(x):
    print(f'Hello {x}')


my_function('Rafi')
# Hello Rafi

def my_function(x):
    s = x**x
    print(s)

my_function(3)
# 27



# 081 Positional vs. Keyword Arguments

# Functions with more than one input 
def my_function(name, location):
    print(f'Hello {name}')
    print(f'How is it like in {location}')

my_function('Rafi', "Dhaka")
# Hello Rafi
# How is it like in Dhaka

# The first argument always translates to the first parameter put in 
my_function('Dhaka', 'Rafi')
# Hello Dhaka
# How is it like in Rafi

# To bypass that
my_function(location = 'Dhaka', name = 'Rafi')
# Hello Rafi
# How is it like in Dhaka





# 082 [Interactive Coding Exercise] Paint Area Calculator

# You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can. 

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 * 4) / 5 

#                          = 1.6

# But because you can't buy 0.6 of a can of paint, the **result should be rounded up** to **2** cans. 

# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.


def wall_paint(h, w, c):
    import math
    s = math.ceil(h*w/c)
    print(f"You'll need {s} cans of paint")

wall_paint(2, 4, 5)




# 083 [Interactive Coding Exercise] Prime Number Checker

# **You need to write a function** that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# # Hint
# 1. Remember the modulus

def prime_checker(number):
    isPrime = True
    for i in range (2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("it's a prime")
    else:
        print("it's not a prime")


n = int(input("Check this number: "))
prime_checker(number=n)




# 084 Caesar Cipher Part 1 - Encryption

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    revised_text = ''
    for l in plain_text:
        position = alphabet.index(l)
        new_position = position + shift_amount
        if new_position > 25:
            new_position = new_position -25 - 1
        new_letter = alphabet[new_position]
        revised_text += new_letter
    print(revised_text)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(plain_text = text, shift_amount = shift)

# clever alternative, just extend the list of alphabets another cycle

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    revised_text = ''
    for l in plain_text:
        position = alphabet.index(l)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        revised_text += new_letter
    print(revised_text)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(plain_text = text, shift_amount = shift)




# 085 Caesar Cipher Part 2 - Decryption

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. \
# Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    revised_text = ''
    for l in plain_text:
        position = alphabet.index(l)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        revised_text += new_letter
    print(revised_text)

def decrypt (plain_text, shift_amount):
    revised_text = ''
    for l in plain_text:
        position = alphabet.index(l)
        # a bug might happen here, what if the position is 0? If we shift 5 places, it will be -5, i.e. index error
        # gotta find a way so that the positioning starts from the second cycle of the letters
        # On second thought, if it is -5, the indexing should start from the end, i.e. z being -1
        # so it works out actually
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        revised_text += new_letter
    print(revised_text)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encrypt':
    encrypt(plain_text = text, shift_amount = shift)
elif direction == 'decrypt':
    decrypt(plain_text = text, shift_amount = shift)




# 086 Caesar Cipher Part 3 - Reorganising our Code

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(plain_text, shift_amount, input_direction):
    revised_text = ''
    for l in plain_text:
        position = alphabet.index(l)
        new_position = 0
        if input_direction == 'encode':
            new_position = position + shift_amount
        elif input_direction == 'decode':
            new_position = position - shift_amount
        new_letter = alphabet[new_position]
        revised_text += new_letter
    print(revised_text)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caeser(plain_text = text, shift_amount = shift, input_direction = direction)








# 087 Caesar Cipher Part 4 - User Experience Improvements & Final Touches
# Timestamp - 03:05

#TODO-1: Import and print the logo from art.py when the program starts.
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#TODO-3: What happens if the user enters a number/symbol/space?
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(plain_text, shift_amount, input_direction):
    revised_text = ''
    for l in plain_text:
        if l in alphabet:
            position = alphabet.index(l)
            if input_direction == 'encode':
                new_position = position + shift_amount
                # caution - one might input 'encode' and then put negative number.
                # suggestion - if shift_amount > 0:
            elif input_direction == 'decode':
                new_position = position - shift_amount
                # caution - one might input 'decode' and then put positive number.
                # suggestion - if shift_amount < 0:
            new_letter = alphabet[new_position]
            # caution - if someone types anything other than encode or decode, none of the if/elif will execute,
            # it will move straight to the line above
            revised_text += new_letter
        else:
            revised_text += l
    print(f'Your {input_direction}d word is {revised_text}')

import cipher_art
print(cipher_art.logo)

continue_game = True
while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    # We do not need an if statement, because if shift is less than 26 (eg. 14), modulus will give 14 (remainder)

    caeser(plain_text = text, shift_amount = shift, input_direction = direction)
    if input('Do you want to continue? (Y/N) - ') == 'N':
        continue_game = False
print('Goodbye')





# 088 How You Can _Stay_ Motivated