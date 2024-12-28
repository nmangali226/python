import random  # Import the random module to allow random selection by the computer

# ASCII art representation for Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# ASCII art representation for Paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# ASCII art representation for Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create a list to hold the three choices for the computer
computer = [rock, paper, scissors]

# Randomly select one of the three choices for the computer
computer_choice = random.choice(computer)

# Ask the user for their choice and convert it to an integer
user_choice = int(input("Please choose 0 for rock, 1 for paper and 2 for scissors: "))

# Check if the user chose Rock
if user_choice == 0:
    print(rock)  # Display the user's choice (Rock)
    if computer_choice == paper:  # If the computer chose Paper
        print(f"computer choice : {paper}")  # Display the computer's choice
        print("you lose")  # User loses
    elif computer_choice == rock:  # If the computer also chose Rock
        print(f"computer choice : {rock}")
        print("Draw")  # It's a tie
    else:  # If the computer chose Scissors
        print(f"computer choice : {scissors}")
        print("you won")  # User wins

# Check if the user chose Paper
elif user_choice == 1:
    print(paper)  # Display the user's choice (Paper)
    if computer_choice == scissors:  # If the computer chose Scissors
        print(f"computer choice : {scissors}")  # Display the computer's choice
        print("you lose")  # User loses
    elif computer_choice == paper:  # If the computer also chose Paper
        print(f"computer choice : {paper}")
        print("Draw")  # It's a tie
    else:  # If the computer chose Rock
        print(f"computer choice : {rock}")
        print("you won")  # User wins

# Check if the user chose Scissors
elif user_choice == 2:
    print(scissors)  # Display the user's choice (Scissors)
    if computer_choice == rock:  # If the computer chose Rock
        print(f"computer choice : {rock}")  # Display the computer's choice
        print("you lose")  # User loses
    elif computer_choice == scissors:  # If the computer also chose Scissors
        print(f"computer choice : {scissors}")
        print("Draw")  # It's a tie
    else:  # If the computer chose Paper
        print(f"computer choice : {paper}")
        print("you won")  # User wins

# Handle invalid input from the user
else:
    print("please choose only 0,1 and 2")  # Prompt the user to choose a valid number
