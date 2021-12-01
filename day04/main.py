# Rock Paper Scissors

import random


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

# put choices into list for easier access
choices_list = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
# input validation
options_list = ["0", "1", "2"]
while True:
    player_choice_str = input("> ")
    if player_choice_str not in options_list:
        print("Invalid choice. Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    else:
        break

# changing the data type to int
player_choice = int(player_choice_str)
print(choices_list[player_choice])

# computer's choice
cpu_choice = random.randint(0, 2)
print("Computer chose:")
print(choices_list[cpu_choice])

# evaluate the choices
if player_choice == cpu_choice:
    print("It's a tie.")
elif (player_choice == 0 and cpu_choice == 2):
    print("You win.")
elif(player_choice == 1 and cpu_choice == 0):
    print("You win.")
elif (player_choice == 2 and cpu_choice == 1):
    print("You win.")
# anything else means the cpu wins
else:
    print("You lose.")
