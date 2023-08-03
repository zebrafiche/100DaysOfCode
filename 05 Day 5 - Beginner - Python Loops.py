# 048 Day 5 Goals_ what we will make by the end of the day 

# By the end of the day, we are going to build a password generator 
# Asks for how many letters and symbols i'd like and build me a pass 





# 049 Using the for loop with Python Lists 

# for loops 

fruits = ['apples', 'peach', 'pear']
for i in fruits:
    print(i)
# apples
# peach
# pear
    print(i, 'pie')
# apples pie
# peach pie
# pear pie




# 050 [Interactive Coding Exercise] Average Height 

# You are going to write a program that calculates the average student height from a List of heights. 
# e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`
# The average height can be calculated by adding all the heights together and dividing by the total number of heights. 
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

# There are a total of **7** heights in `student_heights`
# 1146 ÷ 7 = **163.71428571428572**
# Average height rounded to the nearest whole number = **164**

# **Important** You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their 
# functionality using what you have learnt about for loops.

# # Example Input 
# ```
# 156 178 165 171 187
# ```
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

user_res = input("Input a list of student heights ")
student_heights = user_res.split()
# The str.split(), when not passed any arguments, demilits the string in the spaces 

for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

total_height = 0
num_heights = 0
for j in student_heights:
    total_height = total_height + j
    num_heights = num_heights + 1

print(round(total_height/num_heights))





# 051 [Interactive Coding Exercise] High Score 

# You are going to write a program that calculates the highest score from a List of scores. 
# e.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`

# **Important** you are not allowed to use the max or min functions. The output words must match the example. i.e 
# > `The highest score in the class is: x`

# # Example Input 
# ```
# 78 65 89 86 55 91 64 89
# ```

# In this case, student_scores would be a list that looks like: `[78, 65, 89, 86, 55, 91, 64, 89]`

# # Example Output 
# ```
# The highest score in the class is: 91
# ```


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
for i in student_scores:
    if i > max:
        max = i
print(f'The highest score in the class is: {max}')




# 052 for loops and the range() function

for number in range (start, stop, step)

# find the summation of 1 through 100

sum = 0
for i in range (1, 101):
    sum += i
print(sum)




# 053 [Interactive Coding Exercise] Adding Even Numbers 

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. 
# It should just print the final total and not every step of the calculation.

# # Hint

# 1. There are quite a few ways of solving this problem, but you will need to use the `range()` function in any of the solutions.

sum = 0
for i in range (2, 101, 2):
    sum += i
print(sum)

# Alternative

sum2 = 0
for i in range (1, 101):
    if i % 2 == 0:
        sum2 = sum2 + i
print(sum2)




# 054 [Interactive Coding Exercise] The FizzBuzz Job Interview Question 

# You are going to write a program that automatically prints the solution to the FizzBuzz game. 

# > `Your program should print each number from 1 to 100 in turn.` 
# > `When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 
# > `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
# > `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

# e.g. it might start off like this:

# ```
# `1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz`
# ```

# `.... etc.`

# # Hint

# 1. Remember your answer should start from 1 and go up to and including 100. 

# 2. Each number/text should be printed on a separate line.

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)




# 055 Day 5 Project_ Create a Password Generator 

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
# The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge. 


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password  = ''
possible_chars = [letters, numbers, symbols]

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
for i in range (1, nr_letters+1):
    password = password + ' ' + random.choice(letters)
for j in range (1, nr_numbers+1):
    password  = password + ' ' + random.choice(numbers)
for k in range (1, nr_symbols+1):
    password = password + ' ' + random.choice(symbols)


print(password)

# Hard
# Now change the string to a list
pass_list = password.split()
print(pass_list)
# Now shuffle the items in the said list 
random.shuffle(pass_list)
print(pass_list)
# Now convert the shuffled list to a string 
final_pass = ''
for m in pass_list:
    final_pass += m
print(final_pass)




# 056 Hard Work and Perseverance beats Raw Talent Every Time 