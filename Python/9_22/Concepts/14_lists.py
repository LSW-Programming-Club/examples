#!/usr/bin/env python3

# Create a list with different data types
myList = ["Item 1", 2, 3.5, True]

# For every item in the list state it's type
for item in myList:
    print(type(item))

print(myList)
# For every item in the list change it's value to index number
for index in range(len(myList)):
    myList[index] = index

# Insert a string in to the middle of the list
myList.insert(2,"I'm not supposed to be here")
print(myList)

# Append another string to the list
myList.append("I'm at the end!")
print(myList)

myList.remove(2) # Removes the 2 entry in the list
print(myList)

myList.pop(2) # Removes the 3rd entry in the list
myList.pop(-1) # Removes the last entry in the list
print(myList)

myList.sort(reverse=True) # Sorts list numerically backwards
print(myList)
