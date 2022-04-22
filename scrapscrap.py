import copy,random

# end = (random.randint(0,4),4)
# start = (random.randint(0,4),0)
# modifiedStartX,modifiedStartY = start
# modifiedStartX *=2
# modifiedStartY *= 2
# modifiedEndX,modifiedEndY = end
# modifiedEndX *= 2
# modifiedEndY *= 2
# curr = start
# board = [[0]*5 for i in range(5)]
# visited = []
# visited.append(curr)

# def isMazeComplete(board,start,end,visited):
#     srow,scol = start
#     frow,fcol = end
#     if board[srow][scol] == 1 and board[frow][fcol] == 1 and len(visited) >=11:
#         return True
#     return False

# def isValid(board,loc,row,col,visited):
#     if (loc[0] < 0 or loc[0]>=row) or (loc[1] < 0 or loc[1]>=col):
#         return False
#     elif loc in visited:
#         return False
#     elif board[loc[0]][loc[1]] == 1:
#         return False
#     return True

# def randomizer():
#     possibleMoves = [(0,1),(0,-1),(1,0),(-1,0)]
#     finalMove = []
#     while len(possibleMoves) != 0:
#         index = random.randint(0,len(possibleMoves)-1)
#         finalMove.append(possibleMoves[index])
#         possibleMoves.pop(index)
#     return finalMove

# #change board later to be 10x10
# def mazeGeneration(board,curr,start,end,visited):
#     srow,scol = start
#     board[srow][scol] = 1
#     if isMazeComplete(board,start,end,visited):
#         return board
#     possibleMoves = randomizer()
#     for k in possibleMoves:
#         drow = curr[0] + k[0]
#         dcol = curr[1] + k[1]
#         #curr = (drow,dcol)
#         if isValid(board,(drow,dcol),5,5,visited):
#             board[drow][dcol] = 1
#             visited.append((drow,dcol))
#             solution = mazeGeneration(board,(drow,dcol),start,end,visited)
#             if solution != None:
#                 return solution
#             else:
#                 board[curr[0]][curr[1]] = 0
#                 visited.remove((drow,dcol))
#     return None

# def actualMazeGenerator():
#     newBoard = [[0]*9 for i in range(9)]
#     currBoard = mazeGeneration(board,curr,start,end,visited)
#     newVisited = []
#     counter = 0
#     for (elementX,elementY) in visited:
#         newVisited.append((elementX*2,elementY*2))
#         for (x,y) in newVisited:
#             newBoard[x][y] = 1
#     while counter<len(newVisited)-1:
#         next = counter+1
#         if newVisited[next][0]-newVisited[counter][0] == 2:
#             newBoard[newVisited[next][0]-1][newVisited[next][1]] = 1
#         if newVisited[next][0]-newVisited[counter][0] == -2:
#             newBoard[newVisited[next][0]+1][newVisited[next][1]] = 1
#         if newVisited[next][1]-newVisited[counter][1] == 2:
#             newBoard[newVisited[next][0]][newVisited[next][1]-1] = 1
#         if newVisited[next][1]-newVisited[counter][1] == -2:
#             newBoard[newVisited[next][0]][newVisited[next][1]+1] = 1
#         counter += 1
#     return newBoard

# #helper function for visualizing list
# def repr2dList(L):
#     if (L == []): return '[]'
#     output = [ ]
#     rows = len(L)
#     cols = max([len(L[row]) for row in range(rows)])
#     M = [['']*cols for row in range(rows)]
#     for row in range(rows):
#         for col in range(len(L[row])):
#             M[row][col] = repr(L[row][col])
#     colWidths = [0] * cols
#     for col in range(cols):
#         colWidths[col] = max([len(M[row][col]) for row in range(rows)])
#     output.append('[\n')
#     for row in range(rows):
#         output.append(' [ ')
#         for col in range(cols):
#             if (col > 0):
#                 output.append(', ' if col < len(L[row]) else '  ')
#             output.append(M[row][col].rjust(colWidths[col]))
#         output.append((' ],' if row < rows-1 else ' ]') + '\n')
#     output.append(']')
#     return ''.join(output)

#------------------------------------------------------
# from cmu_112_graphics import *

# def appStarted(app):
#     d = gameDimensions(app)
#     app.margin = d[4]
#     app.rows = d[0]
#     app.cols = d[1]
#     app.cellHeight = d[2]
#     app.cellWidth = d[3]
#     app.board = [[0]*app.cols for i in range(app.rows)]

#     n = newGameDimensions(app)
#     app.newMargin = n[4]
#     app.newRows = n[0]
#     app.newCols = n[1]
#     app.newCellHeight = n[2]
#     app.newCellWidth = n[3]
#     app.newBoard = [[0]*app.newCols for i in range(app.newRows)]

#     app.r = app.cellHeight/2 #17.5
    
#     app.visited = []
#     app.end = (random.randint(0,4),4)
#     app.start = (random.randint(0,4),0)
#     (app.currY,app.currX) = app.start
#     app.currY*=2
#     app.currX*=2

#     app.isMazeOver = False

#     mazeBoardGenerator(app)

# def gameDimensions(app):
#     rows = 5
#     cols = 5
#     margin = 45
#     cellHeight = (app.height-(2*margin))/rows #35
#     cellWidth = app.width/10 #32
#     return (rows, cols, cellHeight, cellWidth, margin)

# def newGameDimensions(app):
#     rows = 9
#     cols = 9
#     margin = 45
#     cellHeight = (app.height-(2*margin))/rows #35
#     cellWidth = app.width/15 #32
#     return (rows, cols, cellHeight, cellWidth, margin)

# def drawMazeCell(app,canvas,row,col,color):
#     h = app.newCellHeight
#     w = app.newCellWidth
#     startX = app.width/4
#     startY = app.newMargin
#     canvas.create_rectangle(startX + col*w, 
#         startY + row*h, 
#         col*w + w + startX, 
#         row*h + h + startY, 
#         fill = color,
#         outline = "black", 
#         width = 2)

# def drawStartCell(app,canvas,start):
#     greenY,greenX = start
#     greenY*=2
#     greenX*=2
#     h = app.newCellHeight
#     w = app.newCellWidth
#     startX = app.width/4
#     startY = app.margin
#     canvas.create_rectangle(startX + greenX*w, 
#         startY + greenY*h, 
#         greenX*w + w + startX, 
#         greenY*h + h + startY, 
#         fill = "green",
#         outline = "green", 
#         width = 2)

# def drawEndCell(app,canvas,end):
#     redY,redX = end
#     redY*=2
#     redX*=2
#     h = app.newCellHeight
#     w = app.newCellWidth
#     startX = app.width/4
#     startY = app.margin
#     canvas.create_rectangle(startX + redX*w,
#         startY + redY*h, 
#         redX*w + w + startX, 
#         redY*h + h + startY, 
#         fill = "red",
#         outline = "red",
#         width = 2)

# def drawMazeBoard(app,canvas):
#     startX = app.width/4
#     startY = app.newMargin
#     canvas.create_rectangle(startX, 
#         startY, 
#         startX + app.newCols*app.newCellWidth, 
#         startY + app.newRows*app.newCellHeight,
#         outline = "red", width = 2)
#     for r in range(app.newRows):
#         for c in range(app.newCols):
#             if app.newBoard[r][c] == 0:
#                 drawMazeCell(app, canvas, r, c,"blue")
#             else:
#                 drawMazeCell(app,canvas,r,c,"pink")

# def repr2dList(L):
#     if (L == []): return '[]'
#     output = [ ]
#     rows = len(L)
#     cols = max([len(L[row]) for row in range(rows)])
#     M = [['']*cols for row in range(rows)]
#     for row in range(rows):
#         for col in range(len(L[row])):
#             M[row][col] = repr(L[row][col])
#     colWidths = [0] * cols
#     for col in range(cols):
#         colWidths[col] = max([len(M[row][col]) for row in range(rows)])
#     output.append('[\n')
#     for row in range(rows):
#         output.append(' [ ')
#         for col in range(cols):
#             if (col > 0):
#                 output.append(', ' if col < len(L[row]) else '  ')
#             output.append(M[row][col].rjust(colWidths[col]))
#         output.append((' ],' if row < rows-1 else ' ]') + '\n')
#     output.append(']')
#     return ''.join(output)

# def drawMazeBarry(app,canvas):
#     canvas.create_oval((app.currX*app.newCellWidth)+(app.width/4)+app.r/2,
#         (app.currY*app.newCellHeight)+(app.margin),
#         (app.currX*app.newCellWidth)+(app.width/4)+(1.5*app.r),
#         (app.currY*app.newCellHeight)+(app.newMargin)+(app.r),
#         fill = "blue")

# def moveMazeBarry(app,x,y):
#     app.currY += y
#     app.currX += x
#     #if Barry is not legal return Barry to previous state
#     if moveMazeBarryIsLegal(app,app.currX,app.currY) == False:
#         app.currY -= y
#         app.currX -= x
#         return False
#     if app.currX == app.end[1]*2 and app.currY == app.end[0]*2:
#         app.isMazeOver = True

# def moveMazeBarryIsLegal(app,currX,currY):
#     if currX<0 or currX>len(app.newBoard[0])-1:
#         return False
#     if currY<0 or currY>len(app.newBoard)-1:
#         return False
#     if app.newBoard[currY][currX] == 0:
#         return False
#     return True

# def mazeOverSplash(app,canvas):
#     canvas.create_rectangle(0,
#         0,
#         app.width,
#         app.height,
#         fill = "white")
#     canvas.create_text(app.width/2,
#         app.height/2-app.margin, 
#         text = "Game Over", 
#         fill = "black",
#         font = "Krungthep 30 bold")

# #----------------------------------------------------------------------

# def isMazeComplete(app):
#     if app.visited[-1] == app.end:
#         return True
#     return False

# def isValid(app,loc):
#     if (loc[0] < 0 or loc[0]>=app.rows) or (loc[1] < 0 or loc[1]>=app.cols):
#         return False
#     elif loc in app.visited:
#         return False
#     elif app.board[loc[0]][loc[1]] == 1:
#         return False
#     return True

# def randomizer(app):
#     finalMove = []
#     possibleMoves = [(0,1),(0,-1),(1,0),(-1,0)]
#     while len(possibleMoves) != 0:
#         index = random.randint(0,len(possibleMoves)-1)
#         finalMove.append(possibleMoves[index])
#         possibleMoves.pop(index)
#     return finalMove

# #change board later to be 10x10
# def mazeGeneration(app,curr):
#     srow,scol = app.start
#     app.board[srow][scol] = 1
#     if isMazeComplete(app):
#         return app.board
#     possibleMoves = randomizer(app)
#     for k in possibleMoves:
#         drow = curr[0] + k[0]
#         dcol = curr[1] + k[1]
#         #curr = (drow,dcol)
#         if isValid(app,(drow,dcol)):
#             app.board[drow][dcol] = 1
#             app.visited.append((drow,dcol))
#             solution = mazeGeneration(app,(drow,dcol))
#             if solution != None:
#                 return solution
#             else:
#                 app.board[curr[0]][curr[1]] = 0
#                 app.visited.remove((drow,dcol))
#     return None

# def actualMazeGenerator(app):
#     newVisited = []
#     counter = 0
#     newBoard = [[0]*app.newCols for i in range(app.newRows)]
#     for (elementX,elementY) in app.visited:
#         newVisited.append((elementX*2,elementY*2))
#         for (x,y) in newVisited:
#             newBoard[x][y] = 1
#     while counter<len(newVisited)-1:
#         next = counter+1
#         if newVisited[next][0]-newVisited[counter][0] == 2:
#             newBoard[newVisited[next][0]-1][newVisited[next][1]] = 1
#         if newVisited[next][0]-newVisited[counter][0] == -2:
#             newBoard[newVisited[next][0]+1][newVisited[next][1]] = 1
#         if newVisited[next][1]-newVisited[counter][1] == 2:
#             newBoard[newVisited[next][0]][newVisited[next][1]-1] = 1
#         if newVisited[next][1]-newVisited[counter][1] == -2:
#             newBoard[newVisited[next][0]][newVisited[next][1]+1] = 1
#         counter += 1
#     return newBoard

# def mazeBoardGenerator(app):
#     curr = app.start
#     app.visited = []
#     app.visited.append(curr)
#     mazeGeneration(app,curr)
#     app.newBoard = actualMazeGenerator(app)
# #----------------------------------------------------------------------
# def keyPressed(app,event):
#     if event.key == "r":
#         appStarted(app)
#     if event.key == "Up":
#         moveMazeBarry(app,0,-1)
#     if event.key == "Down":
#         moveMazeBarry(app,0,1)
#     if event.key == "Right":
#         moveMazeBarry(app,1,0)
#     if event.key == "Left":
#         moveMazeBarry(app,-1,0)

# def redrawAll(app,canvas):
#     canvas.create_rectangle(0, 0, app.width, app.height, fill="orange")
#     drawMazeBoard(app,canvas)
#     drawStartCell(app,canvas,app.start)
#     drawEndCell(app,canvas,app.end)
#     drawMazeBarry(app,canvas)
#     if app.isMazeOver == True:
#         mazeOverSplash(app,canvas)

# def playJetpackMazeride():
#     runApp(width = 800, height = 400)
# #--------------------------------
# playJetpackMazeride()


# print((modifiedStartX,modifiedStartY))
# print((modifiedEndX,modifiedEndY))
# print(repr2dList(mazeGeneration(board,curr,start,end,visited)))
# print(repr2dList(actualMazeGenerator()))

import turtle, string

name = turtle.textinput("username", "Please enter your username:")

print("Hello", name.upper() + "!")