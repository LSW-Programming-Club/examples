#!/usr/bin/env python3

from random import randint

# Ask the user how many games they want to play
bestOf = 0
while not bestOf % 2 or bestOf < 1:
    try:
        bestOf = int(input("Best of how many games? "))
    except:
        print("Try again. That's not an integer")
    else:
        if bestOf < 1:
            print("That's not enough games")
        elif not bestOf % 2:
            print("Even numbers aren't allowed!")

# Set the player's scores
computer = 0
user = 0

while (bestOf+1)/2 not in (computer, user):
    # Computer chooses randomly
    computerChoice = randint(0,2)

    # While the user hasn't selected a valid choice keep asking
    userChoice = 3
    while userChoice == 3:
        userInput = input("Rock Paper or Scissors? ").lower()[0]
        match userInput:
            case "r":
                userChoice = 0
                print("Rock")
            case "p":
                userChoice = 1
                print("Paper")
            case "s":
                userChoice = 2
                print("Scissors")
            case other:
                print("Didn't understand input. Input [R]ock [P]aper or [S]cissors")
    # Print what the user is going against
    print("VS")
    match computerChoice:
        case 0:
            print("Rock")
        case 1:
            print("Paper")
        case 2:
            print("Scissors")
    
    # Check the math to see who won
    if computerChoice == userChoice:
        print("You tied!")
    elif computerChoice - userChoice in (-2,1):
        computer += 1
        print("You lost that round!")
    else:
        user += 1
        print("You won that round!")
    
    # Print the current round winnings
    print("Player: " + str(user))
    print("Computer: " + str(computer))

# Print the final winner
if computer > user:
    print("You lose!")
else:
    print("You win!")