

# def generateCoins(app):
#     if app.scrollX%1000 == 0:
#         app.finalCoinList = []
#         randomIndex = random.randint(0,len(app.coinList)-1)
#         currCoin = app.coinList[randomIndex]
#         coinRow = random.randint(0,12)
#         coinCol = 55
#         for r in range(len(currCoin)):
#             for c in range(len(currCoin[0])):
#                 if currCoin[r][c] == True:
#                     (cx,cy) = ((coinCol+c)*app.cellWidth/2,((coinRow+r)*app.cellHeight/2)+2*app.margin)
#                     app.finalCoinList.append((cx,cy))

# def moveCoin(app,x):
#     app.newCoinList = []
#     for (cx,cy) in app.finalCoinList:
#         (newCx,newCy) = (cx-x,cy)
#         app.newCoinList.append((newCx,newCy))

# def drawCoin(app,canvas,x):
#     coinR = app.r/2
#     for (cx,cy) in app.newCoinList:
#         canvas.create_oval(cx-coinR,
#             cy-coinR,
#             cx+coinR,
#             cy+coinR,
#             fill = "gold", 
#             outline = "yellow", 
#             width = 3)

# def coinCollision(app,x):
#     for (cx,cy) in app.newCoinList:
#         if math.sqrt((cy-app.BarryY)**2+(cx-x-app.BarryX)**2)<=2*app.r:
#             app.newCoinList.remove((cx,cy))
#             app.coinCount += 1

# def coinRemove(app,x):
#     if coinCollision(app,x) == True:
#         app.coinCount += 1
