
def createProbabilityBoard(height, width):
 #create a 2D board given height and width to hold probabilites
    board = []
    for i in range(height):
        current = []
        for j in range(width):
            current.append(0)
        board.append(current)
    return boardxw

def getReward(action, rewardBoard):
    pass

def selectAction(probabilityBoard, rewardBoard):
#loop until board converges? 
# select action using E-Greedy action selection method? maybe? 
    action = #insert E-Greedy cap
    reward = getReward(action, rewardBoard)
    averageReward = 
    probabilityBoard = updateProbabilites(probabilityBoard, reward, averageReward)
    pass

def updateProbabilites(probabiltyBoard, reward, averageReward):
#update probabilites based on stochastic gtadient ascent algorithm
    pass



