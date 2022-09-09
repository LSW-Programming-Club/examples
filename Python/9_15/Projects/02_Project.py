#!/usr/bin/env python3

valid = False

while not valid:
    try:
        userInput = int(input("Input an integer that is divisible by 3 and 5: "))
    except:
        print("That isn't an integer!")
    else:
        if userInput % 15 == 0:
            print("That's divisible by both 3 and 5!")
            valid = True
        elif userInput % 5 == 0:
            print("That's only divisible by 5!")
        elif userInput % 3 == 0:
            print("That's only divisible by 3!")
        else:
            print("That's not divisible by 3 or 5!")
    finally:
        print("\n")
