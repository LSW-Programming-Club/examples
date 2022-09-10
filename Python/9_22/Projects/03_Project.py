#!/usr/bin/env python3

groceryList = ["Apples", "Oranges", "Bananas"]

while len(groceryList):
    print(groceryList)
    userInput = input("What item should I remove? ")
    try:
        userInput = int(userInput)
    except:
        if userInput in groceryList:
            groceryList.remove(userInput)
        else:
            print("That's not on our list!")
    else:
        if userInput < len(groceryList):
            groceryList.pop(userInput)
        else:
            print("That's out of range of the list!")
    finally:
        print("\n")
