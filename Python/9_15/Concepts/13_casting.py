#!/usr/bin/env python3

try: # Attempt this
    userInput = int(input("Type any integer: "))
except: # If error do this
    print("That's not an integer!")
else: # If no error do this
    print(userInput)
