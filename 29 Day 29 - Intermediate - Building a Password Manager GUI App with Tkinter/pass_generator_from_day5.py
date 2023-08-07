# Instructions

# The program will ask:
# ```
# How many letters would you like in your password?
# ```
# ```
# How many symbols would you like?
# ```
# ```
# How many numbers would you like?
# ```
# The objective is to take the inputs from the user to these questions and then generate a random password.
# Use your knowledge about Python lists and loops to complete the challenge.


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Slight modification, so it does not need any input
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# Comment these out
# password = ''
# possible_chars = [letters, numbers, symbols]


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# for i in range(1, (nr_letters + nr_numbers + nr_symbols)+1):

#     if possible_chars[random.randint(0,2)] == letters:
#         password = password + letters[random.randint(0, nr_letters-1)]
#     elif possible_chars[random.randint(0,2)] == numbers:
#         password  = password + numbers[random.randint(0, nr_numbers-1)]
#     elif possible_chars[random.randint(0,2)] == symbols:
#         password = password + symbols[random.randint(0, nr_symbols-1)]

# Easy
# for i in range(1, nr_letters+1):
#     password = password + ' ' + random.choice(letters)
# for j in range(1, nr_numbers+1):
#     password = password + ' ' + random.choice(numbers)
# for k in range(1, nr_symbols+1):
#     password = password + ' ' + random.choice(symbols)

# Use list comprehension here instead to bypass these for loops above

pass_letters = [random.choice(letters) for i in range(1, nr_letters + 1)]
pass_numbers = [random.choice(numbers) for j in range(1, nr_numbers+1)]
pass_symbols = [random.choice(symbols) for k in range(1, nr_symbols+1)]
# initially we had a password string which we converted to a list, we will get the list directly now
pass_list = pass_letters + pass_numbers + pass_symbols


# Hard
# Now change the string to a list
# pass_list = password.split()
# print(pass_list)
# Now shuffle the items in the said list
random.shuffle(pass_list)
# print(pass_list)
# Now convert the shuffled list to a string
# final_pass = ''
# for m in pass_list:
#     final_pass += m
# use join() here instead
final_pass = ''.join(pass_list)
print(final_pass)




# 056 Hard Work and Perseverance beats Raw Talent Every Time