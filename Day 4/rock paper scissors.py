rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

# Users Input
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Print player's choice using ASCII art
print("Player's choice:")
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("Invalid choice. Please choose 0, 1, or 2.")

# Computers Input
comp_choice = random.randint(0, 2)

# Print computer's choice using ASCII art
print("Computer's choice:")
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)

if (player_choice == comp_choice):
    print("You Tied.")
elif (player_choice == 1 and comp_choice == 0) or (player_choice == 2 and comp_choice == 1) or (player_choice == 0 and comp_choice == 2):
    print("You Win!")
else:
    print("You Lose")