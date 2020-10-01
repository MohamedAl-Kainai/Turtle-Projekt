from turtle import *

# screen
bgcolor("Gray")
# ----------- #

''' Spieler 1 Settings '''
Spieler1 = Turtle()
Spieler1.color('red','green')

name = textinput("TextInput", "Name of first player:")
Spieler1.name = name.title()

# Spieler position
Spieler1.penup()
Spieler1.setpos(100,0)
Spieler1.pendown()
Spieler1.left(90)

Spieler1.POSITON_ON_SCREEN = []

''' Spieler 1 Bewegung '''
def Look_Up():
    if Spieler1.heading() != 90.0:
        Spieler1.setheading(90)

def Look_Down():
    if Spieler1.heading() != 270.0:
        Spieler1.setheading(270)

def Look_Left():
    if Spieler1.heading() != 180.0:
        Spieler1.setheading(180)

def Look_Right():
    if Spieler1.heading() != 0.0:
        Spieler1.setheading(0.0)

def Go_und_position_speichern():
    _forward = 30
    for i in range(_forward*2):
        Spieler1.POSITON_ON_SCREEN.append(Spieler1.position())
        Spieler1.forward(.5)
        if Spieler1.position() in Spieler1.POSITON_ON_SCREEN:
            print (Spieler1.name,'is Crach')

onkey(Look_Up,'Up')
onkey(Look_Down,'Down')
onkey(Look_Left,'Left')
onkey(Look_Right,'Right')
onkey(Go_und_position_speichern,'space')


''' Spieler 2 Settings '''
Spieler2 = Turtle()
Spieler2.color('blue','white')

name = textinput("TextInput", "Name of second player:")
Spieler2.name = name.title()

# Spieler position
Spieler2.penup()
Spieler2.setpos(-100,0)
Spieler2.pendown()
Spieler2.left(90)

Spieler1.speed(0.01)
listen()
done()
