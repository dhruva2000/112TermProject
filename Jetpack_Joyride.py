import math, copy, random
from cmu_112_graphics import *
#------------------------------------------------------------------------------
def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)
#------------------------------------------------------------------------------
def appStarted(app):
    d = gameDimensions(app)
    app.margin = d[4]
    app.rows = d[0]
    app.cols = d[1]
    app.cellHeight = d[2]
    app.cellWidth = d[3]
    app.empty = "white"
    app.board = [[app.empty]*app.cols for i in range(app.rows)]
    #--------------------------------------------------------------------------
    app.r = app.cellHeight/2 #17.5
    app.BarryY = (app.height-(app.margin)-app.r)
    app.BarryX = (5*app.cellWidth)+app.r
    app.move = 0
    #--------------------------------------------------------------------------
    app.scrollX = 0
    # app.coinList = [(random.randrange(835,1155,32),random.randrange(43,358,35)) for i in range(50)]
    app.TP = [
        [True, True, True, False, True, True, True],
        [False, True, False,False, True, False,True],
        [False, True, False,False, True, True, True],
        [False, True, False,False, True, False, False]
    ]
    app.rectangle = [
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True]
    ]
    app.circle = [
        [False, False, True, True, False, False],
        [False, True, True, True, True, False],
        [False, True, True, True, True, False],
        [False, False, True, True, False, False]
    ]
    app.upArrow = [
        [False, False, False,True, False, False, False],
        [False, False, True, True, True, False, False],
        [False, True,  True, False, True, True,  False],
        [True,  True, False, False, False,True,  True],
        [True, False, False, False, False, False,True]
    ]
    app.downArrow = [
        [True, False, False,False, False, False, True],
        [True, True, False, False, False, True, True],
        [False, True,  True, False, True, True, False],
        [False,  False, True, True, True, False, False],
        [False, False, False, True, False, False,False]
    ]
    app.coinList = [app.TP,app.rectangle,app.circle,app.upArrow,app.downArrow]
    app.finalCoinList = []
    app.newCoinList = []
    #--------------------------------------------------------------------------
    app.staticLaser = True
    app.staticLaserDimensions = ()
    app.rotatingLaser = True
    app.missile = True
    app.obstacleList=[app.staticLaser,app.rotatingLaser,app.missile]
    app.obstacleCount = 1
    app.coinCount = 0
    #--------------------------------------------------------------------------
    app.isGameOver = False
    app.reset = False
    app.speed = 1
    app.distance = 0
    app.score = app.coinCount + app.distance
    generateObstacles(app)
    generateCoins(app)

#------------------------------------------------------------------------------
def gameDimensions(app):
    rows = 10
    cols = 32
    margin = 45
    cellHeight = (app.height-(2*margin))/rows #35
    cellWidth = app.width/25 #32
    return (rows, cols, cellHeight, cellWidth, margin)

def keyPressed(app,event):
    if event.key == "Up":
        app.move = -10
    if event.key == "Down":
        app.move = 10
    if event.key == "r":
        appStarted(app)
#------------------------------------------------------------------------------
def drawCell(app,canvas,row,col,color):
    h = app.cellHeight
    w = app.cellWidth
    startX = 0
    startY = app.margin
    canvas.create_rectangle(startX + col*w, 
        startY + row*h, 
        col*w + w + startX, 
        row*h + h + startY, 
        fill = color,
        outline = "black", 
        width = 3)

def drawGameBoard(app,canvas):
    for r in range(app.rows):
        for c in range(app.cols):
            color = app.board[r][c]
            drawCell(app, canvas, r, c, color)

def resetBoard(app):
    if len(app.finalCoinList)>0:
        app.finalCoinList = []

def drawEndScreen(app,canvas):
    canvas.create_rectangle(0,
        0,
        app.width,
        app.height,
        fill = "white")
    canvas.create_text(app.width/2,
        app.height/2-app.margin, 
        text = "Game Over", 
        fill = "black",
        font = "Krungthep 30 bold")
    canvas.create_text(app.width/2,
        app.height/2 + app.margin,
        text = "Press r to restart",
        fill = "black",
        font = "Krungthep 26 bold")
    canvas.create_text(app.width/2,
        app.height/2,
        text = f"Coins = {app.coinCount}",
        fill = "black",
        font = "Krungthep 26 bold")


def drawScoreTracker(app,canvas):
    canvas.create_text(app.width/2,
    app.margin/2,
    text = f"Score = {app.coinCount+app.distance}",
    fill = "black",
    font = "Krungthep 15 bold")
    
#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------
def generateObstacles(app):
    # randomIndex = random.randint(0,len(app.obstacleList)-1)
    # currObs = app.obstacleList[randomIndex]
    currObs = app.staticLaser
    # if currObs == app.rotatingLaser:
        #generateRotatingLaser(app)
        # height = random.randint(3,6)
        # start = (26*app.cellWidth,)
        # pass
    # if currObs == app.missile:
    #     #generateMissile(app)
    #     pass
    if currObs == app.staticLaser:
        height = random.randint(0,4)
        width = random.randint(2,5)
        #find the starting circle and place it randomly on the grid
        start = (26*app.cellWidth,random.randint(height*app.cellHeight+app.margin,app.height-app.margin-height*app.cellHeight))
        app.staticLaserDimensions = (height,width,start)

def drawStaticLaser(app,canvas,dimensions,x):
    (height,width,start) = dimensions
    (cx,cy) = start
    (finalCx,finalCy) = (cx+width*app.cellWidth,cy+height*app.cellHeight)
    canvas.create_oval(cx-app.r-2*x,
        cy-app.r,
        cx+app.r-2*x,
        cy+app.r,
        fill = "red",
        outline = "gold",
        width = 3)
    canvas.create_oval(finalCx-app.r-2*x,
        finalCy-app.r,
        finalCx+app.r-2*x,
        finalCy+app.r,
        fill = "red",
        outline = "gold",
        width = 3)
    canvas.create_line(cx-2*x,
        cy,
        finalCx-2*x,
        finalCy,
        fill = "red",
        width = 10)

def collisionDetectionLaser(app,dimensions,x,barryX,barryY):
    (height,width,start) = dimensions
    (cx,cy) = start
    (newcx,newcy) = (cx-2*x,cy)
    (finalCx,finalCy) = (newcx+width*app.cellWidth,newcy+height*app.cellHeight)
    gradient = (finalCy-newcy)/(finalCx-newcx)
    if math.sqrt((finalCy-barryY)**2+(finalCx-barryX)**2)<=2*app.r:
        return True
    if math.sqrt((newcy-barryY)**2+(newcx-barryX)**2)<=2*app.r:
        return True
    #Use equation of line to solve for y coordinate
    if (newcx<=barryX<=finalCx):
        # print(barryY,(gradient*(barryX-newcx)+newcy))
        # print(abs((barryY-(gradient*abs((barryX-newcx))+newcy))),app.r)
        if abs((barryY-(gradient*abs((barryX-newcx))+newcy)))<=app.r:
            return True
    return False
#------------------------------------------------------------------------------
def generateCoins(app):
    app.newCoinList = []
    app.finalCoinList = []
    randomIndex = random.randint(0,len(app.coinList)-1)
    currCoin = app.coinList[randomIndex]
    coinRow = random.randint(0,12)
    coinCol = 55
    for r in range(len(currCoin)):
        for c in range(len(currCoin[0])):
            if currCoin[r][c] == True:
                (cx,cy) = ((coinCol+c)*app.cellWidth/2,((coinRow+r)*app.cellHeight/2)+2*app.margin)
                app.finalCoinList.append((cx,cy))

def collideCoin(app,x):
    app.newCoinList = []
    for (cx,cy) in app.finalCoinList:
        (newCx,newCy) = (cx-x,cy)
        if math.sqrt((newCy-app.BarryY)**2+(newCx-app.BarryX)**2)<=app.r+max(app.cellHeight/2,app.cellWidth/2):
            app.coinCount += 1
            app.finalCoinList.remove((cx,cy))
        else:
            app.newCoinList.append((newCx,newCy))
            
    
def drawCoin(app,canvas,i):
    coinR = app.r/2
    (cx,cy) = i
    canvas.create_oval(cx-coinR,
        cy-coinR,
        cx+coinR,
        cy+coinR,
        fill = "gold", 
        outline = "yellow", 
        width = 3)

#----------------------------
def timerFired(app):
    moveBarry(app,app.move)
    if app.isGameOver == False:
        app.scrollX += 8*app.speed
        app.distance += 1
        if app.scrollX%900==0:
            app.scrollX = 0
            generateObstacles(app)
        if app.scrollX%1000==0:
            generateCoins(app)
        if app.distance % 50 == 0:
            app.speed += 0.2
        collideCoin(app,app.scrollX)
        # coinCollision(app,app.scrollX)
        if collisionDetectionLaser(app,app.staticLaserDimensions,app.scrollX,app.BarryX,app.BarryY) == True:
            app.isGameOver = True

def redrawAll(app,canvas):
    if app.isGameOver == False:
        drawGameBoard(app,canvas)
        drawBarry(app,canvas)
        for i in app.newCoinList:
            drawCoin(app,canvas,i)
        drawStaticLaser(app,canvas,app.staticLaserDimensions,app.scrollX)
        drawScoreTracker(app,canvas)
    elif app.isGameOver == True:
        drawEndScreen(app,canvas)

def playJetpackJoyride():
    runApp(width = 800, height = 400)
#------------------------------------------------------------------------------
playJetpackJoyride()


#To-do
#1) Keep track of scores and number of obstacles and coins collected
#2) Create an end game screen
#3) Create a restart button