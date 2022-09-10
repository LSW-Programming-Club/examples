#!/usr/bin/env python3

def readConfig():
    with open("settings.txt", "r") as f:
        return f.read()

def writeConfig(string):
    with open("settings.txt", "w") as f:
        f.write(string)

def toggle(index, config): 
    if "True" in config[index]:
        config[index] = config[index].replace("True","False")
    else:
        config[index] = config[index].replace("False", "True")
    config = config[0] + "\n" + config[1] + "\n" + config[2]
    writeConfig(config)

while True:
    config = readConfig()
    print(config)
    config = config.split("\n")
    try:
        userInput = int(input("What setting should I change? "))
    except:
        print("That's not an integer!")
    else:
        if userInput < 3:
            toggle(userInput, config)
        else:
            print("That integer is too large!")