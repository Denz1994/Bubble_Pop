

######################################################################
# Author: Dr. Jan Pearce
# username: pearcej
#
# Purpose: demonstration of event-driven programming using the turtle library
# for a kind of user interface
######################################################################
# Acknowledgements: Mario Nakazawa added the quit_box
######################################################################

import time
import turtle
import random
import sys

def draw_header(t_text):
    ''' Create turtle for header'''
    header = turtle.Turtle()
    header.penup()
    header.setpos(-10,150)
    header.write("Click one of the big choices",move=False,align='center',font=("Arial",30,("bold","normal")))
    header.hideturtle()
    t_text.penup()
    t_text.setpos(0,-150)
    t_text.hideturtle()

def draw_one(t_one):
    '''draws one shape'''
    t_one.color("purple")
    t_one.shapesize(3)
    t_one.penup()
    t_one.setpos(-100,20)
    t_one.shape("circle")

def draw_two(t_two):
    '''draws two shapes'''
    t_two.color("#0000FF")
    t_two.shapesize(3)
    t_two.penup()
    t_two.setpos(100,20)
    t_two.shape("circle")
    t_two.stamp()
    t_two.color("#000099")
    t_two.setpos(110,25)
    t_two.stamp()

def display_many(numb):
    '''called to display numb many circles of random colors'''
    turtle.colormode(255)
    position=-150
    for i in range(numb):
        num = turtle.Turtle()
        num.shape("circle")
        num.color(random.randrange(256),random.randrange(256),random.randrange(256))
        num.penup()
        num.setposition(position+20*i, 130)
        num.stamp()

def draw_quit(t_quit):
    '''draws quit box shape'''
    t_quit.penup()
    t_quit.hideturtle()
    t_quit.setpos(-60,-200)
    t_quit.write("Click to stop ->",move=False,align='center',font=("Courier New",15,("bold","normal")))
    t_quit.showturtle()
    t_quit.setpos(60,-190)
    t_quit.shapesize(1,1,15)
    t_quit.shape("square")
    t_quit.color("#AFA4AF")

def handler_one(x, y):
    '''called when circle one is clicked'''
    wn.title("1 clicked")
    text.clear()
    text.write("1 clicked",move=False,align='center',font=("Arial",30,("bold","normal")))
    # add more code here for when the user clicks 1

def handler_two(x, y):
    '''called when circle two is clicked'''
    wn.title("2 clicked")
    text.clear()
    text.write("2 clicked",move=False,align='center',font=("Arial",30,("bold","normal")))
    # add more code here for when the user clicks 2

def handler_quit(x, y):
    '''called by pressing quit_box turtle to quit'''
    text.clear()
    text.write("Quitting",move=False,align='center',font=("Arial",30,("bold","normal")))
    time.sleep(1)
    wn.bye()
    # sys.exit(0)

def main():
    ''' main function'''
    turtle.colormode(255)
    global wn
    wn = turtle.Screen()  # Get a reference to the window

    global text
    text = turtle.Turtle()     # Create turtle for text

    draw_header(text)

    one = turtle.Turtle()      # Create turtle for choice of 1
    draw_one(one)

    two = turtle.Turtle()     # Create turtle for choice of 2
    draw_two(two)

    quit_box = turtle.Turtle()     # use a "quitter" turtle to stop the loop.
    draw_quit(quit_box)

    wn.listen()
    while True:     #main loop
        #numb=8 # we could allow the user to enter this.
        quit_box.onclick(handler_quit)
        one.onclick(handler_one)
        two.onclick(handler_two)
        #display_many(numb)
    wn.bye()

main()