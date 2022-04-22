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
    app.mazeBoard = [[0]*5 for i in range(5)]
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
    app.powerUpDimensions = ()
    app.newPowerUpDimensions = (1,2)
    app.powerUpCounter = 0
    app.powerUp = []
    app.powerUpRemove = 0
    app.powerUpCounter = 0
    app.rotatingLaser = True
    app.missile = True
    app.obstacleList=[app.staticLaser,app.missile]
    app.obstacleCount = 1
    app.coinCount = 0
    #--------------------------------------------------------------------------
    app.gameStart = False
    app.pause = False
    app.gameMode = "normal"
    app.isGameOver = False
    app.reset = False
    app.speed = 1
    app.distance = 0
    app.score = app.coinCount + app.distance
    app.highScoreFile = "/Users/dhruvareddy/Documents/GitHub/112TermProject/highScore.txt"
    highScore = open(app.highScoreFile,"r")
    app.highScore = highScore.read()
    app.leaderBoardDisplay = False
    app.currentUser = ""
    #--------------------------------------------------------------------------
    n = newGameDimensions(app)
    app.newMargin = n[4]
    app.newRows = n[0]
    app.newCols = n[1]
    app.newCellHeight = n[2]
    app.newCellWidth = n[3]
    app.newBoard = [[0]*app.newCols for i in range(app.newRows)]

    app.visited = []
    app.end = (4,4)
    app.start = (0,0)
    (app.currY,app.currX) = app.start
    app.currY*=2
    app.currX*=2

    app.timeElapsed = 100
    app.mazeCompletedCounter = 0
    

    #--------------------------------------------------------------------------
    generateObstacles(app)
    generateCoins(app)
    generatePowerUp(app)
    mazeBoardGenerator(app)
    # getUserName(app)

#------------------------------------------------------------------------------
def gameDimensions(app):
    rows = 10
    cols = 32
    margin = 45
    cellHeight = (app.height-(2*margin))/rows #35
    cellWidth = app.width/25 #32
    return (rows, cols, cellHeight, cellWidth, margin)

def keyPressed(app,event):
    if app.isGameOver == False:
        if app.gameMode == "normal":
            if event.key == "Up":
                app.move = -10
            if event.key == "Down":
                app.move = 10
            if event.key == "r":
                appStarted(app)
        if app.gameMode == "maze":
            if event.key == "Up":
                moveMazeBarry(app,0,-1)
            if event.key == "Down":
                moveMazeBarry(app,0,1)
            if event.key == "Right":
                moveMazeBarry(app,1,0)
            if event.key == "Left":
                moveMazeBarry(app,-1,0)
        if app.pause == False:
            if event.key == "s":
                app.gameStart = True
    if app.isGameOver == True:
        if event.key == "r":
                appStarted(app)
        if event.key == "h":
            app.leaderBoardDisplay = not app.leaderBoardDisplay
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

def drawStartScreen(app,canvas):
    canvas.create_rectangle(0,
        0,
        app.width,
        app.height,
        fill = "white")
    canvas.create_text(app.width/2,
        app.height/2-app.margin, 
        text = "Welcome to Jetpack Mazeride", 
        fill = "black",
        font = "Krungthep 30 bold")
    canvas.create_text(app.width/2,
        app.height/2 + app.margin,
        text = "Press s to start",
        fill = "black",
        font = "Krungthep 26 bold")

def drawEndScreen(app,canvas):
    canvas.create_rectangle(0,
        0,
        app.width,
        app.height,
        fill = "white")
    canvas.create_text(app.width/2,
        app.height/2-2*app.margin, 
        text = "Game Over", 
        fill = "black",
        font = "Krungthep 30 bold")
    canvas.create_text(app.width/4,
        app.height/2 - app.margin,
        text = f"Coins = {app.coinCount}",
        fill = "black",
        font = "Krungthep 26 bold")
    canvas.create_text(3*app.width/4,
        app.height/2 - app.margin,
        text = f"Mazes Completed = {app.mazeCompletedCounter}",
        fill = "black",
        font = "Krungthep 26 bold")
    canvas.create_text(app.width/4,
        app.height/2,
        text = f"Raw Score = {(app.coinCount+app.distance)}",
        fill = "black",
        font = "Krungthep 26 bold")
    canvas.create_text(3*app.width/4,
        app.height/2,
        text = f"Final Score = {(app.coinCount+app.distance)*app.mazeCompletedCounter}",
        fill = "black",
        font = "Krungthep 26 bold")
    canvas.create_text(app.width/2,
        app.height/2 + app.margin,
        text = "Press h for highscore",
        fill = "black",
        font = "Krungthep 26 bold")
    canvas.create_text(app.width/2,
        app.height/2 + 2*app.margin,
        text = "Press r to restart",
        fill = "black",
        font = "Krungthep 26 bold")

def drawScoreTracker(app,canvas):
    canvas.create_text(app.width/5,
    app.margin/2,
    text = f"Score = {(app.coinCount+app.distance)}",
    fill = "black",
    font = "Krungthep 30 bold")

def drawHighScore(app,canvas):
    canvas.create_rectangle(0,
        0,
        app.width,
        app.height,
        fill = "white")
    canvas.create_text(app.width/2,
        app.height/2,
        text = f"Highscore = {app.highScore}",
        fill = "black",
        font = "Krungthep 30 bold")

def updateHighScore(app):
    if ((app.coinCount+app.distance)*app.mazeCompletedCounter)>int(app.highScore):
        with open(app.highScoreFile,"w") as highScoreFileToWrite:
            highScoreFileToWrite.write(str((app.coinCount+app.distance)*app.mazeCompletedCounter))
    highScore = open(app.highScoreFile,"r")
    app.highScore = highScore.read()

def getUserName(app):
    # from turtle import 
    app.currUser = input("Enter your username here: ")
    app.pause = False
    
#----------------------------------main player----------------------------------
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
#---------------------------------obstacles-------------------------------------
def generateObstacles(app):
    # randomIndex = random.randint(0,len(app.obstacleList)-1)
    # currObs = app.obstacleList[randomIndex]
    currObs = app.staticLaser
    # if currObs == app.missile:
    #     #generateMissile(app)
    #     pass
    if currObs == app.staticLaser:
        height = random.randint(0,4)
        width = random.randint(2,5)
        #find the starting circle and place it randomly on the grid
        start = (26*app.cellWidth,random.randint(height*app.cellHeight+app.margin,
        app.height-app.margin-height*app.cellHeight))
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
        updateHighScore(app)
        return True
    if math.sqrt((newcy-barryY)**2+(newcx-barryX)**2)<=2*app.r:
        updateHighScore(app)
        return True
    #Use equation of line to solve for y coordinate
    if (newcx<=barryX<=finalCx):
        # print(barryY,(gradient*(barryX-newcx)+newcy))
        # print(abs((barryY-(gradient*abs((barryX-newcx))+newcy))),app.r)
        if abs((barryY-(gradient*abs((barryX-newcx))+newcy)))<=app.r:
            updateHighScore(app)
            return True
    return False
#-----------------------------------coins---------------------------------------
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
                (cx,cy) = ((coinCol+c)*app.cellWidth/2,
                ((coinRow+r)*app.cellHeight/2)+2*app.margin)
                app.finalCoinList.append((cx,cy))

def collideCoin(app,x):
    app.newCoinList = []
    for (cx,cy) in app.finalCoinList:
        (newCx,newCy) = (cx-x,cy)
        if math.sqrt((newCy-app.BarryY)**2+(newCx-app.BarryX)**2)<=app.r+max(app.cellHeight/2,app.cellWidth/2):
            app.coinCount += 1
            app.finalCoinList.remove((cx,cy))
        # if newCy-app.BarryY<app.cellHeight and newCx-app.BarryX < app.cellWidth:
        #     app.coinCount += 1
        #     app.finalCoinList.remove((cx,cy))
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
#---------------------------------power ups-------------------------------------
def generatePowerUp(app):
    app.powerUpRemove = 0
    srow,scol = (random.randint(3,8),27)
    cx,cy = scol*app.cellWidth + app.r,srow*app.cellHeight + app.r + app.margin
    app.powerUpDimensions = (cx,cy)

def collidePowerUp(app,x,counter):
    cx,cy = app.powerUpDimensions
    if app.powerUpRemove == 0:
        app.powerUp = [(cx,cy)]
        yDirections = [0,0.5,0,-0.5]
        index = counter%len(yDirections)
        y = yDirections[index]*app.cellHeight
        (newCx,newCy) = (cx-x,cy+y)
        app.newPowerUpDimensions = (newCx,newCy)
        if math.sqrt((newCy-app.BarryY)**2+(newCx-app.BarryX)**2)<=app.r+max(app.cellHeight/2,app.cellWidth/2):
            app.powerUp.remove((cx,cy))
            app.powerUpRemove = 1
            app.gameMode = "maze"
            mazeBoardGenerator(app)

def drawPowerUp(app,canvas,dimensions):
    coinR = app.r
    (cx,cy) = dimensions
    canvas.create_oval(cx-coinR,
        cy-coinR,
        cx+coinR,
        cy+coinR,
        fill = "purple", 
        outline = "yellow", 
        width = 3)
#------------------------------maze mode----------------------------------

def newGameDimensions(app):
    rows = 9
    cols = 9
    margin = 45
    cellHeight = (app.height-(2*margin))/rows #35
    cellWidth = app.width/15 #32
    return (rows, cols, cellHeight, cellWidth, margin)

def drawMazeCell(app,canvas,row,col,color):
    h = app.newCellHeight
    w = app.newCellWidth
    startX = app.width/4
    startY = app.newMargin
    canvas.create_rectangle(startX + col*w, 
        startY + row*h, 
        col*w + w + startX, 
        row*h + h + startY, 
        fill = color,
        outline = "black", 
        width = 2)

def drawMazeBoard(app,canvas):
    startX = app.width/4
    startY = app.newMargin
    canvas.create_rectangle(startX, 
        startY, 
        startX + app.newCols*app.newCellWidth, 
        startY + app.newRows*app.newCellHeight,
        outline = "red", width = 2)
    for r in range(app.newRows):
        for c in range(app.newCols):
            if app.newBoard[r][c] == 0:
                drawMazeCell(app, canvas, r, c,"blue")
            else:
                drawMazeCell(app,canvas,r,c,"pink")

def drawStartCell(app,canvas,start):
    greenY,greenX = start
    greenY*=2
    greenX*=2
    h = app.newCellHeight
    w = app.newCellWidth
    startX = app.width/4
    startY = app.margin
    canvas.create_rectangle(startX + greenX*w, 
        startY + greenY*h, 
        greenX*w + w + startX, 
        greenY*h + h + startY, 
        fill = "green",
        outline = "green", 
        width = 2)

def drawEndCell(app,canvas,end):
    redY,redX = end
    redY*=2
    redX*=2
    h = app.newCellHeight
    w = app.newCellWidth
    startX = app.width/4
    startY = app.margin
    canvas.create_rectangle(startX + redX*w, 
        startY + redY*h, 
        redX*w + w + startX, 
        redY*h + h + startY, 
        fill = "red",
        outline = "red",
        width = 2)

def repr2dList(L):
    if (L == []): return '[]'
    output = [ ]
    rows = len(L)
    cols = max([len(L[row]) for row in range(rows)])
    M = [['']*cols for row in range(rows)]
    for row in range(rows):
        for col in range(len(L[row])):
            M[row][col] = repr(L[row][col])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(M[row][col]) for row in range(rows)])
    output.append('[\n')
    for row in range(rows):
        output.append(' [ ')
        for col in range(cols):
            if (col > 0):
                output.append(', ' if col < len(L[row]) else '  ')
            output.append(M[row][col].rjust(colWidths[col]))
        output.append((' ],' if row < rows-1 else ' ]') + '\n')
    output.append(']')
    return ''.join(output)

def drawMazeBarry(app,canvas):
    canvas.create_oval((app.currX*app.newCellWidth)+(app.width/4)+app.newCellWidth/2-app.r,
        (app.currY*app.newCellHeight)+(app.margin)-app.r+app.newCellHeight/2,
        (app.currX*app.newCellWidth)+(app.width/4)+app.newCellWidth/2+(app.r),
        (app.currY*app.newCellHeight)+(app.newMargin)+app.newCellHeight/2+(app.r),
        fill = "blue")

def moveMazeBarry(app,x,y):
    app.currY += y
    app.currX += x
    #if Barry is not legal return Barry to previous state
    if moveMazeBarryIsLegal(app,app.currX,app.currY) == False:
        app.currY -= y
        app.currX -= x
        return False
    if app.currX == app.end[1]*2 and app.currY == app.end[0]*2:
        app.timeElapsed = 100
        app.mazeCompletedCounter += 1
        app.gameMode = "normal"

def moveMazeBarryIsLegal(app,currX,currY):
    if currX<0 or currX>len(app.newBoard[0])-1:
        return False
    if currY<0 or currY>len(app.newBoard)-1:
        return False
    if app.newBoard[currY][currX] == 0:
        return False
    return True

def drawMazeCounter(app,canvas):
    canvas.create_text(3*app.width/4,
        app.margin/2, 
        text = f"Mazes Completed = {app.mazeCompletedCounter}", 
        fill = "black",
        font = "Krungthep 30 bold")

def isMazeComplete(app):
    if app.visited[-1] == app.end:
        return True
    return False

def isValid(app,loc):
    if (loc[0] < 0 or loc[0]>4) or (loc[1] < 0 or loc[1]>4):
        return False
    elif loc in app.visited:
        return False
    elif app.board[loc[0]][loc[1]] == 1:
        return False
    return True

def randomizer(app):
    finalMove = []
    possibleMoves = [(0,1),(0,-1),(1,0),(-1,0)]
    while len(possibleMoves) != 0:
        index = random.randint(0,len(possibleMoves)-1)
        finalMove.append(possibleMoves[index])
        possibleMoves.pop(index)
    return finalMove

def mazeGeneration(app,curr):
    srow,scol = app.start
    app.mazeBoard[srow][scol] = 1
    if isMazeComplete(app):
        return app.mazeBoard
    possibleMoves = randomizer(app)
    for k in possibleMoves:
        drow = curr[0] + k[0]
        dcol = curr[1] + k[1]
        #curr = (drow,dcol)
        if isValid(app,(drow,dcol)):
            app.mazeBoard[drow][dcol] = 1
            app.visited.append((drow,dcol))
            solution = mazeGeneration(app,(drow,dcol))
            if solution != None:
                return solution
            else:
                app.mazeBoard[curr[0]][curr[1]] = 0
                app.visited.remove((drow,dcol))
    return None

def actualMazeGenerator(app):
    newVisited = []
    counter = 0
    newBoard = [[0]*app.newCols for i in range(app.newRows)]
    for (elementX,elementY) in app.visited:
        newVisited.append((elementX*2,elementY*2))
        for (x,y) in newVisited:
            newBoard[x][y] = 1
    while counter<len(newVisited)-1:
        next = counter+1
        if newVisited[next][0]-newVisited[counter][0] == 2:
            newBoard[newVisited[next][0]-1][newVisited[next][1]] = 1
        if newVisited[next][0]-newVisited[counter][0] == -2:
            newBoard[newVisited[next][0]+1][newVisited[next][1]] = 1
        if newVisited[next][1]-newVisited[counter][1] == 2:
            newBoard[newVisited[next][0]][newVisited[next][1]-1] = 1
        if newVisited[next][1]-newVisited[counter][1] == -2:
            newBoard[newVisited[next][0]][newVisited[next][1]+1] = 1
        counter += 1
    return newBoard

def mazeBoardGenerator(app):
    app.end = (random.randint(0,4),4)
    app.start = (random.randint(0,4),0)
    x,y = app.start
    (app.currX,app.currY) = (y*2,x*2)
    curr = (x,y)
    app.visited = []
    app.visited.append(curr)
    mazeGeneration(app,curr)
    app.newBoard = actualMazeGenerator(app)

def mazeCompleted(app):
    redY,redX = app.end
    endY,endX = redY*2,redX*2
    if app.currX == endX and app.currY == endY:
        return True
    return False

def drawTimeElapsedMazeSplash(app,canvas):
    canvas.create_text(app.width/2,
        app.margin/2.1, 
        text = f"Time Elapsed = {app.timeElapsed}", 
        fill = "black",
        font = "Krungthep 25 bold")


#-----------------------timer fired and redraw all------------------------------
def timerFired(app):
    if app.gameStart == False:
        pass
    else:
        if app.isGameOver == False:
            print(f"mazeCompletedCounter = {app.mazeCompletedCounter}")
            print(f"scrollX = {app.scrollX}")
            print(f"time elapsed = {app.timeElapsed}")
            if app.gameMode == "maze":
                app.scrollX = 0
                app.timeElapsed -= 1
                if mazeCompleted(app):
                    app.timeElapsed = 100
                    app.mazeCompletedCounter += 1
                    app.powerUpRemove = 0
                    app.gameMode = "normal"
                elif app.timeElapsed == 0:
                    app.timeElapsed = 100
                    app.powerUpRemove = 1
                    app.gameMode = "normal"
            else:
                moveBarry(app,app.move)
                app.scrollX += 8*app.speed
                app.distance += 1
                app.powerUpCounter += 1
                if app.scrollX>=1200:
                    app.scrollX = 0
                    generateObstacles(app)
                if app.scrollX>=1000:
                    generateCoins(app)
                #how to generate more sporadically?
                if app.scrollX>=1100:
                    generatePowerUp(app)
                if app.distance % 50 == 0:
                    app.speed += 0.2
                collideCoin(app,app.scrollX)
                collidePowerUp(app,app.scrollX*1.67,app.powerUpCounter)
                if collisionDetectionLaser(app,app.staticLaserDimensions,
                app.scrollX,app.BarryX,app.BarryY) == True:
                    app.isGameOver = True

def redrawAll(app,canvas):
    if app.isGameOver == False:
        if app.gameStart == False:
            drawStartScreen(app,canvas)
        else:
            if app.gameMode == "maze":
                canvas.create_rectangle(0,0,app.width,app.height,fill="white")
                drawMazeBoard(app,canvas)
                drawStartCell(app,canvas,app.start)
                drawEndCell(app,canvas,app.end)
                drawMazeBarry(app,canvas)
                drawTimeElapsedMazeSplash(app,canvas)
            else:
                drawGameBoard(app,canvas)
                drawBarry(app,canvas)
                for i in app.newCoinList:
                    drawCoin(app,canvas,i)
                if len(app.powerUp)>0:
                    drawPowerUp(app,canvas,app.newPowerUpDimensions)
                drawStaticLaser(app,canvas,app.staticLaserDimensions,app.scrollX)
                drawScoreTracker(app,canvas)
                drawMazeCounter(app,canvas)
    elif app.isGameOver == True:
        drawEndScreen(app,canvas)
        if app.leaderBoardDisplay == True:
            drawHighScore(app,canvas)

def playJetpackJoyride():
    runApp(width = 800, height = 400)
#------------------------------------------------------------------------------
playJetpackJoyride()


#------------------------------citations:--------------------------------------
#From 112 course: Tetris, sidescroller, gameModes, repr2dList, Backtracking Logic
#fontfamily.py: https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter courtesy of jimmiesrustled
#Images and sprites: https://github.com/HugoLaurencon/JetPack-Joyride-game-in-Python/find/master courtesy of Hugo Laurencon
#Open and read txt files: https://www.pythontutorial.net/python-basics/python-read-text-file/, https://www.geeksforgeeks.org/reading-writing-text-files-python/
#Special shoutouts to TAs Grace, Winston and Tjun Jet for their help!!

#current problems:
