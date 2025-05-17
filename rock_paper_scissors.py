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
game_images=[rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice < 0 or user_choice > 2:
    print("Don't you have sense input value between 0 and 2.")
else:
    print("You chose:")
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])
    if user_choice == 1 and computer_choice ==0:
        print("You win baby!")
    elif user_choice == 2 and computer_choice ==1:
        print("You win baby!")
    elif user_choice == 0 and computer_choice ==2:
        print("You win baby!")
    elif user_choice == 0 and computer_choice ==1:
        print("Sorry you lose")
    elif user_choice == 1 and computer_choice ==2:
        print("Sorry you lose")
    elif user_choice == 2 and computer_choice ==0:
        print("Sorry you lose")
    elif user_choice == 0 and computer_choice ==0:
        print("It's a draw.")
    elif user_choice == 1 and computer_choice ==1:
        print("It's a draw.")
    elif user_choice == 2 and computer_choice == 2:
        print("It's a draw.")
