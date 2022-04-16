
from Jetpack_Joyride import *
from Obstacles import *
from Coins import *
from Background import *
from cmu_112_graphics import *

def drawBarry(app,canvas):
    canvas.create_oval(app.BarryX-app.r,
        app.BarryY-app.r,
        app.BarryX+app.r,
        app.BarryY+app.r, 
        fill = "blue")

def moveBarry(app,y):
    app.BarryY += y
    #if Barry is not legal return Barry to previous state
    if moveBarryIsLegal(app) == False:
        if app.BarryY>(app.height-app.margin-app.r):
            app.BarryY = (app.height-app.margin-app.r)
        elif app.BarryY<(app.margin+app.r):
            app.BarryY = (app.margin+app.r)
        return False
    return True

def moveBarryIsLegal(app):
    if app.BarryY<(app.margin+app.r):
        return False
    if app.BarryY>(app.height-(2*app.margin)):
        return False
    return True