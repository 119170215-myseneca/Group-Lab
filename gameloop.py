#!/usr/bin/env python3
import random # used to generate random numbers

while True:
    choice_of_user = input("Which one of the following will you choose to win or lose?(rock, paper, scissors): ")  #this will take input from the users to choose rock,paper and scissors

    possible_action = ["rock", "paper", "scissors"]  # this is for all the possibility

    action_of_computer = random.choice(possible_action) # prints random choice of the computer

    print(f"\nYour choice was {choice_of_user}, but computer chose {action_of_computer}.\n")  

    if choice_of_user == action_of_computer:                                  # this is for the case of tie
       print(f"{choice_of_user} was chose by both of you. You were thinking the same thing. so, it's a tie!")
    elif choice_of_user == "rock":                                   #When user input is rock
       if action_of_computer == "scissors":
         print("Rock kills Scissors! The winner is.... You!")
       else:
         print("Paper wraps rock! You are a loser.")
    elif choice_of_user == "paper":                                 #When user input is paper
       if action_of_computer == "rock":
         print("Paper wraps Rock! The winner is.... You!")
       else:
         print("Scissors cuts down Paper! You are a loser.")
    elif choice_of_user == "scissors":                              #When user input is scissors
       if action_of_computer == "paper":
         print("Scissors cuts down Paper! The winner is.... You!")
       else:
         print("Rock kills Scissors! You are a loser.")

    play_again = input("\nPlay again? (y/n): \n")
    if play_again.lower() != "y":
        break

