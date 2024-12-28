# Importing the random module to enable random selection of items from lists
import random

# List of all alphabetic characters (both lowercase and uppercase)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of numeric characters (digits from 0 to 9)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of special characters (common symbols for password generation)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Displaying a welcome message for the password generator program
print("Welcome to the PyPassword Generator!")

# Prompting the user to input the desired number of letters in their password
nr_letters = int(input("How many letters would you like in your password?\n"))

# Prompting the user to input the desired number of symbols in their password
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Prompting the user to input the desired number of numbers in their password
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Randomly selecting the specified number of letters from the `letters` list
letter = random.sample(letters, nr_letters)

# Randomly selecting the specified number of numbers from the `numbers` list
number = random.sample(numbers, nr_numbers)

# Randomly selecting the specified number of symbols from the `symbols` list
symbol = random.sample(symbols, nr_symbols)

# Combining the selected letters, numbers, and symbols into a single list
password = letter + number + symbol

# Shuffling the combined list to randomize the order of characters in the password
random.shuffle(password)

# Converting the shuffled list of characters into a single string
password = ''.join(password)

# Displaying the generated password to the user
print(f"your password is : {password}")
