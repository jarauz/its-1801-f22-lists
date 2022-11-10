"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

casper = turtle.Turtle()
listOfColors = [ "red", "green", "blue", "yellow"]

for c in listOfColors:
    casper.color(c)
    casper.forward(75)
    casper.left(90)

# The structure ['red', 'green', 'blue', 'yellow'] is also a list

# Print just the first element of listOfColors to the console
print(listOfColors[0])
# Print just the second element of listOfColors to the console
print(listOfColors[1])
# Print just the third element of listOfColors to the console
print(listOfColors[2])
# Print just the fourth element of listOfColors to the console
print(listOfColors[3])
# Print from element 1 to element 2
print(listOfColors[1:3]) 
# Python will print from index 1 to 2 (3 is not included)

print("The available colors are red(0), green(1), blue(2)")
i = input("Please select a color (type the corresponding number): ")
# Remember that input will store the value the
# user types in the variable i which is a string
# First convert it to an integer to use as a list index

newListOfColors = ["red", "green", "blue"]
casper.color(newListOfColors[int(i)])

for c in range(3):
  casper.forward(30)
  casper.left(120)