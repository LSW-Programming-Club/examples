#!/usr/bin/env python3

from datetime import datetime

def greeting():
    name = input("What is your name? ")
    date = datetime.now()
    print("Hello " + name + "!")
    print("Today is: " + str(date))

greeting()
