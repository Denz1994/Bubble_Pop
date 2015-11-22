######################################################################
# Name: event-turtle-onclicl-example.py
# Modified by: Jan Pearce, Scott Heggen, Mario Nakazawa
# username: pearcej, heggens, nakazawam
# Purpose: To demonstrate how turtle object responds to mouse click events.
#
######################################################################
# Acknowledgements:
#
#   This code is adapted from http://openbookproject.net/thinkcs/python/english3e/events.html#mouse-events
#   The wn.mainloop() method, which is implemented for Python version 3.0,
#   was replaced with the mainloop() function in the Tkinter object, which
#   works for version 2.7 used in class.
#
######################################################################

import turtle
import Tkinter      # needed for the mainloop() function


def write_info():
    """ Writes instructions on how to quit the program to the screen """

    text = turtle.Turtle()
    text.penup()
    text.goto(-150, 200)
    text.pendown()
    text.write("Click to draw. Press q to quit.", font=("Arial", 16, "normal") )
    text.penup()
    text.hideturtle()


def main():
    """ Use the mouse to draw a shape on the screen."""

    # Event handler for the mouse click events
    def handler_goto(x, y):
        tess.goto(x, y)

    # Event handler for the q button on the keyboard
    def handler_quitit():
        wn.bye()        # Closes the window

    # Sets up the window
    turtle.setup(400,500)
    wn = turtle.Screen()
    wn.title("How to handle mouse clicks on the window!")
    wn.bgcolor("lightgreen")

    # Writes to the screen how to quit the program
    write_info()

    # Calls the event handler quitit() for onkey events for "q"
    wn.onkey(handler_quitit, "q")

    # Initializes the turtle object that will be doing the drawing
    tess = turtle.Turtle()
    tess.color("purple")
    tess.pensize(3)
    tess.shape("circle")

    # NOTICE that the screen is responding to the click events!
    wn.onclick(handler_goto)        # Wire up a click on the window.
    wn.listen()

    Tkinter.mainloop()              # wn.exitonclick() no longer works because we have an onclick event!
                                    # Replaced the wn.mainloop() method call which does not exist
                                    # in Python version 2.7 with the appropriate one in the
                                    # Tkinter module.

main()