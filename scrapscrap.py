import copy,random

end = (random.randint(0,4),4)
start = (random.randint(0,4),0)
curr = start
board = [[0]*5 for i in range(5)]
visited = []
visited.append(curr)

def isMazeComplete(board,start,end,visited):
    srow,scol = start
    frow,fcol = end
    if board[srow][scol] == 1 and board[frow][fcol] == 1 and len(visited) >= 18:
        return True
    return False

def isValid(board,loc,row,col,visited):
    if (loc[0] < 0 or loc[0]>=row) or (loc[1] < 0 or loc[1]>=col):
        return False
    elif loc in visited:
        return False
    elif board[loc[0]][loc[1]] == 1:
        return False
    return True

def randomizer():
    possibleMoves = [(0,1),(0,-1),(1,0),(-1,0)]
    finalMove = []
    while len(possibleMoves) != 0:
        index = random.randint(0,len(possibleMoves)-1)
        finalMove.append(possibleMoves[index])
        possibleMoves.pop(index)
    return finalMove

#change board later to be 10x10
def mazeGeneration(board,curr,start,end,visited):
    srow,scol = start
    board[srow][scol] = 1
    if isMazeComplete(board,start,end,visited):
        print('visited', visited)
        return board
    possibleMoves = randomizer()
    for k in possibleMoves:
        drow = curr[0] + k[0]
        dcol = curr[1] + k[1]
        #curr = (drow,dcol)
        if isValid(board,(drow,dcol),5,5,visited):
            board[drow][dcol] = 1
            visited.append((drow,dcol))
            solution = mazeGeneration(board,(drow,dcol),start,end,visited)
            if solution != None:
                return solution
            else:
                board[curr[0]][curr[1]] = 0
                visited.remove((drow,dcol))
    return None

# def actualMazeGenerator():
#     newBoard = [[0]*10 for i in range(10)]
#     currBoard = mazeGeneration(board,curr,start,end)
#     for i in range(len(currBoard)):
#         for j in range(len(currBoard[0])):
#             newBoard[i*2][j*2] = currBoard[i][j]
#     for row in range(len(newBoard)):
#         for col in range(len(newBoard)):
#             if row-1>=0:
#                 if row+1<10:
#                     if newBoard[row-1][col] == 1 and newBoard[row+1][col] == 1:
#                         newBoard[row][col] = 1
#             if col-1>=0:
#                 if col+1<10:
#                     if newBoard[row][col-1] == 1 and newBoard[row][col+1] == 1:
#                         newBoard[row][col] = 1
#     return newBoard

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
#     app.newBoard = [[0]*app.cols for i in range(app.rows)]
    
#     app.finalMove = []
#     app.visited = set()
#     app.end = (random.randint(0,4),4)
#     app.start = (random.randint(0,4),0)
#     mazeBoardGenerator(app)
#     print(app.start)
#     print(app.end)
#     print(app.board)
#     pass

# def gameDimensions(app):
#     rows = 5
#     cols = 5
#     margin = 45
#     cellHeight = (app.height-(2*margin))/rows #35
#     cellWidth = app.width/10 #32
#     return (rows, cols, cellHeight, cellWidth, margin)

# def drawCell(app,canvas,row,col):
#     h = app.cellHeight
#     w = app.cellWidth
#     startX = app.width/4
#     startY = app.margin
#     canvas.create_rectangle(startX + col*w, 
#         startY + row*h, 
#         col*w + w + startX, 
#         row*h + h + startY, 
#         fill = "black",
#         outline = "black", 
#         width = 2)

# def drawGameBoard(app,canvas):
#     for r in range(app.rows):
#         for c in range(app.cols):
#             if app.board[r][c] == 1:
#                 drawCell(app, canvas, r, c)

# #----------------------------------------------------------------------

# def isMazeComplete(app):
#     srow,scol = app.start
#     frow,fcol = app.end
#     if app.board[srow][scol] == 1 and app.board[frow][fcol] == 1 and len(app.visited) >= 15:
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
#     possibleMoves = [(0,1),(0,-1),(1,0),(-1,0)]
#     while len(possibleMoves) != 0:
#         index = random.randint(0,len(possibleMoves)-1)
#         app.finalMove.append(possibleMoves[index])
#         possibleMoves.pop(index)
#     return app.finalMove

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
#             app.visited.add((drow,dcol))
#             solution = mazeGeneration(app,(drow,dcol))
#             if solution != None:
#                 return solution
#             else:
#                 app.board[curr[0]][curr[1]] = 0
#                 visited.remove((drow,dcol))
#     return None

# def mazeBoardGenerator(app):
#     curr = app.start
#     app.visited = set()
#     app.visited.add(curr)
#     mazeGeneration(app,curr)
# #----------------------------------------------------------------------
# def redrawAll(app,canvas):
#     canvas.create_rectangle(0, 0, app.width, app.height, fill="orange")
#     drawGameBoard(app,canvas)

# def playJetpackMazeride():
#     runApp(width = 800, height = 400)
# #--------------------------------
# playJetpackMazeride()


print(start)
print(end)
print(mazeGeneration(board,curr,start,end,visited))