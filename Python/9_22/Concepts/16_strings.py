#!/usr/bin/env python3

a = """This
Is a
Multiline
String    """
print(a) # Print whole string
print(a[3]) # Print the 4th letter
print(len(a)) # Print length of string
print("This" in a) # True
print("This" not in a) # False
print(a[0:4]) # Print 1st-5th letters
print(a[-6:]) # Print last 6 letters
print(a.upper()) # Print all uppercase
print(a.replace("I","")) # Remove all I's
# Print all uppercase and remove all I's
print(a.upper().replace("I",""))
# Split the string into a list on every newline
print(a.split("\n"))
# Removes that whitespace at the end before split
print(a.strip().split("\n"))
print(a + "\nNew Data!")
print("You're \"Smart\" ") # Escape quotes
fillInTheBlank = "I am {} and {}"
qualities = ["Old","Sad"]
print(fillInTheBlank.format(qualities[0],qualities[1]))