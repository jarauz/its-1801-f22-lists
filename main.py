"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

casper = turtle.Turtle()

for c in ['red', 'green', 'blue', 'yellow']:
    casper.color(c)
    casper.forward(75)
    casper.left(90)

# The structure [0, 1, 2, 3] in Python is called a list
# The structure ['red', 'green', 'blue', 'yellow'] is also a list

for c in [0, 1, 2, 3]:
  print("The value of c in this iteration is " + str(c))