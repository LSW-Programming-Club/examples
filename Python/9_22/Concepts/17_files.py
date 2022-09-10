#!/usr/bin/env python3

def readFile(file):
    f = open(file,"rt")
    print(f.read())
    f.close()

# Open file in read only mode as a text
f = open("read.txt", "rt")
# Read only the first 2 lines
print(f.readline())
print(f.readline())

print(f.read()) # Read rest of file
f.close() # Close files when done

f = open("write.txt","wt") # Overwrite
f.write("This overwrote everything!")
f.close()

readFile("write.txt")

f = open("write.txt","at") # Append
f.write("\nSneaky extra line\nLine 3")
f.close()

readFile("write.txt")

# The more proper way to open a file for use
with open("read.txt", "rt") as f:
    print(f.read())

with open("write.txt", "at") as f:
    f.write("\nLine 4")

readFile("write.txt")
