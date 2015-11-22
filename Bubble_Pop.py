

######################################################################
# Author: Denzell Barnett
# username: barnettd
# Assignment: CSC 226 Final Project
#
# Purpose: To engage users in a fun game using event-driven programming.
#          Also to build on previously existing code.
######################################################################
# Acknowledgements: Dr. Scott Heggan, Dr. Jan Pearce, Dr.Mario Nakazawa
#                   I would also like to acknowledge Kaamilah Wilson who
#                   became my beta tester for this program.
#                   Lastly, Nintendo's Duck Hunt for the inspiration.
######################################################################

import time
import turtle
import random
import sys
import string

def draw_header(t_text):
    ''' Create turtle for header'''
    header = turtle.Turtle()
    header.hideturtle()
    header.penup()
    header.setpos(-10,250)
    header.write("Click the cirlces to get points.",move=False,align='center',font=("Arial",18,("bold","normal")))
    time.sleep(1)
    header.hideturtle()
    t_text.penup()
    t_text.setpos(0,-150)
    t_text.hideturtle()

def plus_one(score):
    score+=100
    return score

def plus_two(score):
    score+=200
    return score

def plus_four(score):
    score+=400
    return score

def draw_score(score):
    ''' Create turtle for header'''
    header = turtle.Turtle()
    header.shape('blank')
    header.penup()
    header.setpos(-10, -170)
    header.write(score,move=False,align='center',font=("Arial",15,("bold","normal")))
    header.clear()
    header.hideturtle()

def draw_one(t_one):
    '''draws one shape'''
    x = random.randint(-250, 250)
    y = random.randint(-200, 200)
    t_one.hideturtle()
    t_one.color("blue")
    t_one.shapesize(3.5)
    t_one.penup()
    t_one.setpos(x, y)
    t_one.shape("circle")
    t_one.showturtle()

def draw_two(t_two):
    '''draws two shapes'''
    x = random.randint(-250, 250)
    y = random.randint(-200, 200)
    t_two.hideturtle()
    t_two.color("red")
    t_two.shapesize(1.5)
    t_two.penup()
    t_two.setpos(x, y)
    t_two.shape("circle")
    t_two.showturtle()

def draw_four(t_four):
    '''draws two shapes'''
    t_four.shape('blank')

    x = random.randint(-250,250)
    y = random.randint(-200,200)
    t_four.hideturtle()
    t_four.color("purple")
    t_four.shapesize(.27)
    t_four.penup()
    t_four.setpos(x, y)
    t_four.shape("circle")
    t_four.showturtle()

def color(numb):
    #function only used for color mode
    '''called to display numb many circles of random colors'''
    turtle.colormode(255)

def draw_quit(t_quit):
    '''draws quit box shape'''
    t_quit.penup()
    t_quit.hideturtle()
    t_quit.setpos(205,-247)
    t_quit.write("Click to stop ->",move=False,align='center',font=("Courier New",14,("bold","normal")))
    t_quit.showturtle()
    t_quit.setpos(310,-240)
    t_quit.shapesize(1,1,10)
    t_quit.shape("square")
    t_quit.color("#AFA4AF")

def handler_quit(x, y):
    '''called by pressing quit_box turtle to quit'''
    text.clear()
    text.write("Quitting",move=False,align='center',font=("Arial",30,("bold","normal")))
    time.sleep(1)
    wn.bye()
    # sys.exit(0)

def main():
    ''' main function'''

    #Introduction to game with rules.

    print ("\n\n\nWelcome to BUBBLE POP!!!\n")
    instructions=raw_input("Would you like to read the instructions? Type: (yes/no)")
    if instructions.lower()=='yes':
        print ("The goal is to rack up as many points before the game timer ends."
            "You have sixty seconds.\n"
            "The blue ball is worth 100 points.\nThe red ball is worth 200 points.\nThe purple ball is worth 400 points.\n"
            "The game will start soon.\n\n"
            "Click on the new window that will be made at the bottom of the screen in a few seconds and play.")
        time.sleep(18)
    elif instructions.lower()=='no':
        print ('Okay, have fun!!!\n\n Click on the new window that will be made at the bottom of the screen in a few seconds and play.')
        time.sleep(8)

    else:
        print("Okay, I guess that means no.\n\nClick on the new window that will be made at the bottom of the screen in a few seconds and play.")
        time.sleep(8)

    global score
    score=0

    global start
    start=0

    '''
    The handlers have to be defined withing main. I think partly because they use global variables (score).
    '''

    def handler_one(x, y):
        '''called when circle one is clicked'''
        global score
        #score has to be a global variable again
        one.hideturtle()
        text.setpos(-105,-260)
        text.write("+100",move=False,align='center',font=("Arial",25,("bold","normal")))
        #Adds points to total score
        score=plus_one(score)
        print ('Points:\t'+str(score))
        print '\n'*3
        #time.sleep(.2)
        draw_one(one)
        text.clear()

    def handler_two(x, y):
        '''called when circle two is clicked'''
        global score
        #score has to be a global variable again
        two.hideturtle()
        text.setpos(-20,-260)
        text.write("+200",move=False,align='center',font=("Arial",25,("bold","normal")))
        #Adds points to total score
        score=plus_two(score)
        print ('Points:\t'+str(score))
        print '\n'*3
        draw_two(two)
        text.clear()

    def handler_four(x, y):
        '''called when circle two is clicked'''
        global score
        #score has to be a global variable again
        four.hideturtle()
        text.setpos(65,-260)
        text.write("+400",move=False,align='center',font=("Arial",25,("bold","normal")))
        #Adds points to total score
        score=plus_four(score)
        print ('Points:\t'+str(score))
        print '\n'*3
        draw_four(four)
        text.clear()

    def handler_quit(x, y):
        '''called by pressing quit_box turtle to quit'''

        text.clear()
        text.setposition(-20,-260)
        text.write("Quitting",move=False,align='center',font=("Arial",30,("bold","normal")))
        time.sleep(1)
        wn.bye()
        print ('Your final score is:\t'+str(score)+' points!\nThank you for playing!')
        time.sleep(2)
        sys.exit(0)


    turtle.colormode(255)

    global wn
    wn = turtle.Screen()  # Get a reference to the window

    #Makes instructions and text.
    global text
    text = turtle.Turtle()
    draw_header(text)
    wn=turtle.Screen()

    #100 point Turtle created
    one = turtle.Turtle()
    draw_one(one)

    #200 point Turtle created
    two = turtle.Turtle()
    draw_two(two)

    #400 point Turtle created
    four = turtle.Turtle()
    draw_four(four)

    quit_box = turtle.Turtle()     # use a "quitter" turtle to stop the game.
    draw_quit(quit_box)

    wn.listen()

    while True:
            #Creates a timer within the turtle window
            clock=turtle.Turtle()
            clock.shape('blank')
            clock.penup()
            clock.setpos(-280,-250)
            clock.pendown()
            global seconds
            seconds=61

            for i in range(seconds):
                seconds-=1
                clock.write('Time:  '+str(seconds),font=("Arial",15,("bold","normal")))
                time.sleep(1)
                clock.clear()

                #Handler commands for clicking on turtles
                one.onclick(handler_one)
                two.onclick(handler_two)
                four.onclick(handler_four)
                quit_box.onclick(handler_quit)

                #Commands the end of game sequences.
                if seconds ==0:
                    wn.clearscreen()
                    text.setpos(0,0)
                    text.write("Game Over",move=False,align='center',font=("Arial",40,("bold","normal")))
                    time.sleep(3)
                    wn.bye()
                    print ('Your final score is:\t'+str(score)+' points!\nThank you for playing!\n')
                    time.sleep(2)
                    restart=raw_input("Would you like to try again? Type: (yes/no)")
                    global yes
                    global no
                    if restart.lower()=="yes":
                        print '\nCool! Press(Shift+F10)'
                        sys.exit(0)
                    if restart.lower()=='no':
                        print '\nOkay, thank you for playing :)'
                        sys.exit(0)


main()