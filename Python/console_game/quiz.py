#!/usr/bin/env python3

score = 0

if input("What year was the Eiffel Tower built? ") == "1887":
    score+=1

if input("What color is the sky? ").lower() == "blue":
    score += 1

if input("What month did the LSW Programming Club start? ").capitalize() == "September":
    score += 1

print("Your score is: " + str(score) + "/3")
