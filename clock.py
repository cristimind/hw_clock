import turtle


import turtle as t

hours   = 12
minutes = 30
seconds = 15


def printTime():
    print( f' {hours:02}:{minutes:02}:{seconds:02}' )



def DrawClock():
    #clock
    t.color('red')
    t.circle(100)
    t.left(90)
    t.penup()
    t.forward(100)
    t.color('black')


    #hours
    t.pensize(3)
    t.pendown()
    t.right(hours*30)
    t.forward(70)

    #reset
    t.color('gray')
    t.penup
    t.left(180)
    t.forward(70)
    t.right(180-hours*30)

    #minutes
    t.pensize(2)
    t.pendown()
    t.right(minutes*6)
    t.forward(80)

    #reset
    t.penup
    t.left(180)
    t.forward(80)
    t.right(180-minutes*6)
    
    
    
    t.pensize(1)
    t.pendown()
    t.right(seconds*6)
    t.forward(80)








    input('press enter to continue')