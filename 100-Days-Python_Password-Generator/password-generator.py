#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# get random characters from letters equal to len(nr_letters)
# shuffle letters
random.shuffle(letters)
# take characters from front of shuffled list
letters_list = []
for x in range(0, nr_letters):
    letters_list.append(letters[x])

# get random characters from numbers equal to len(nr_numbers)
random.shuffle(numbers)
numbers_list = []
for x in range(0, nr_numbers):
    numbers_list.append(numbers[x])

# get random characters from symbols equal to len(nr_symbols)
random.shuffle(symbols)
symbols_list = []
for x in range(0, nr_symbols):
    symbols_list.append(symbols[x])

# combine lists of characters into one list
letters_list.extend(numbers_list)
letters_list.extend(symbols_list)

# shuffle list
random.shuffle(letters_list)
s = ""
password = s.join(letters_list)

# return list as string
print(f"Your password is: {password}")