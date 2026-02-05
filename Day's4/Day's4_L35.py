Rock = ''' 
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

choice = [Rock,Paper,Scissors]
computer_choice = random.randint(0,2)
# Rock = 0
# paper = 1
# Scissors = 2
your_choice = int(input("Enter your choice, Rock(0), Paper(1) or Scissors(2): "))

if your_choice < 0 or your_choice>2:
    print("Invalid choice")
else:
    print("\nComputer chose:")
    print(choice[computer_choice])

    print("You chose:")
    print(choice[your_choice])

    if your_choice == computer_choice:
        print("It's a tie!")
    elif(
        (your_choice == 0 and computer_choice == 2)or
        (your_choice == 1 and computer_choice == 0)or
        (your_choice == 2 and computer_choice == 1)
        ):
        print("You win!")
    else:
        print("You lose!")

