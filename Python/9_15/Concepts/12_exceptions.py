#!/usr/bin/env python3

# Uncomment the declaration below to have the code run without error
# x = 0

try:  # Run your error prone code in here
    x = x
except:  # Ran if there's an error
    print("An error occurred!")
else:  # Ran if no errors
    print("No error occurred!")
finally:  # Run this no matter what
    print("This prints no matter what")
