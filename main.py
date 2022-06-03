# Rock Paper Scissors Game

import random


def play():
    print("Welcome to Rock-Paper-Scissors\n")

    choices = ["R", "P", "S"]
    choices_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    computer = random.choice(choices)
    user = input("Rock (R), Paper (P) or Scissors (S)?: ").upper()

    while user not in choices:
        print("Invalid choice! Enter (R, P or S)")
        user = input("Rock (R), Paper (P) or Scissors (S)?: ").upper()

    if user == computer:
        print("It's a tie")
        print(f'Player({choices_dict[user]}) : CPU({choices_dict[computer]})')
        play()

    elif is_won(user, computer):
        print("Player won!")
        print(f'Player({choices_dict[user]}) : CPU({choices_dict[computer]})')

    elif not is_won(user, computer):
        print("CPU won!")
        print(f'Player({choices_dict[user]}) : CPU({choices_dict[computer]})')


def is_won(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent =='P') \
            or (player == 'P' and opponent == 'R'):
        return True


play()
input("\nPress the enter key to exit.")
