#!/usr/bin/env python3

# Create a dictionary
myCar = {
    "make": "Honda",
    "model": "Accord",
    "year": 2010
}
print(myCar)

# Print the amount of entries in myCar
print(len(myCar))

# Add the color of myCar
myCar["color"] = "white"
print(myCar)

# Change the year of myCar
myCar["year"] = 2020

# Print the year of myCar
print(myCar.get("year"))

# Remove the make data of myCar
myCar.pop("make")
print(myCar)

# List ever entry in myCar
for data in myCar:
    print(data) # Key
    print(myCar[data]) # Value
