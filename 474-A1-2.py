'''
CISC 474 Assignment 1
Author: Ellie Sekine
Student Number: 20071971
'''

'''
Creates a 2D array of zeros for a given height and width 
'''
def createBoard(height, width):
    board = []
    for i in range(height):
        current = []
        for j in range(width):
            current.append(0)
        board.append(current)
    return board

'''
Finds the state value array for a 2D grid of zeros, where the four actions are up, down left and
right, and the probability of taking any of those actions is 25%. Dimensions of the grid, the location
of A, A', B, B' amd the discount rate gamma are taken as paramaters. Dynamic programming approach is used
'''
def stateValue(A, B, APrime, BPrime, gamma, dimensions):
    theta = 0.001
    delta = float('inf')
    board = createBoard(dimensions[0], dimensions[1])
    policyBoard = createBoard(dimensions[0], dimensions[1])

    while delta > theta:
        #records the the current iterations state values
        newValues = createBoard(dimensions[0], dimensions[1])
        for row in range(dimensions[0]):
            for col in range(dimensions[1]):
                #finds the sum of state value for each possible action that can be taken
                for action in ["U", "D", "L", "R"]:
                    statePrime, reward = rewardMap(board, A, B, APrime, BPrime, action, row, col)
                    newValues[row][col] += 0.25 * (reward + gamma*board[statePrime[0]][statePrime[1]])
        sum = 0
        #finds the difference between the state values in the previous board's iteration and the current boards
        for row in range(len(board)):
            for column in range(len(board)):
                sum += abs(newValues[row][column] - board[row][column])  
        delta = sum 
        #sets board to be our most recent iterations values
        board = newValues
        policyBoard = updatePolicy(board, policyBoard)
    #rounds the values of the state value board
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col] = round(board[row][col],1) 
    return (board, policyBoard)

'''
Maps a given an action to a reward and the location of a state prime. Takes the board, locations of
A, A', B and B', the action being take, and the row and column of the current state are taken as
paramaters
'''
def rewardMap(board, A, B, APrime, BPrime, action, row, col):
    #if the action takes you to A
    if row == A[0] and col == A[1]:
        reward = 10
        sPrime = (APrime[0], APrime[1])
    #if the action takes you to B
    elif row == B[0] and col == B[1]:
        reward = 5
        sPrime = (BPrime[0], BPrime[1])
    #if the action takes you to a normal spot on the grid
    elif action == "U" and row != 0:
        reward = 0
        sPrime = (row-1, col)
    elif action == "D" and row < len(board)-1:
        reward = 0
        sPrime = (row+1, col)
    elif action == "R" and col < len(board[row])-1:
        reward = 0
        sPrime = (row, col+1)
    elif action == "L" and col != 0:
        reward = 0
        sPrime = (row, col-1)
    #if the action takes you off the board
    else:
        reward = -1
        sPrime = (row, col)
    return (sPrime, reward)

def updatePolicy(valueBoard, policyBoard):
    for row in range(len(valueBoard)):
        for col in range(len(valueBoard)):
            policyBoard[row][col] = greedPolicy(valueBoard, row, col)
    return policyBoard


def greedPolicy(valueBoard, row, col):
    up = {'U':float('-inf')}
    down = {'D': float('-inf')}
    left = {'L':float('-inf')}
    right = {'R':float('-inf')}
    policies = {'U': float('-inf'), 'D' : float('-inf'), 'L' : float('-inf'), 'R': float('-inf') }
    if row != 0:
        policies['U'] = valueBoard[row-1][col]
    if row < len(valueBoard)-1:
        policies['D'] = valueBoard[row + 1][col]
    if col != 0:
        policies['L'] = valueBoard[row][col-1]
    if col < len(valueBoard[row])-1:
        policies['R'] = valueBoard[row][col+1]
    

    bestPolicy = max(policies, key=policies.get)
    return bestPolicy


#indicies for A, A' and B, B' are given in 1-based, so they are adjusted by subtracting 1
A = [1-1, 2-1]
APrime = [5-1,2-1] 
B = [1-1,4-1]
BPrime = [3-1,4-1]
gamma = 0.85
boards = stateValue(A,B,APrime, BPrime, gamma, [5,5])

print('5x5 for gamma of 0.85')
print(boards[0])
print(boards[1])

gamma = 0.75 
board = stateValue(A,B,APrime, BPrime, gamma, [5,5])

print('5x5 for gamma of 0.75')
print(board)

A = [3-1, 2-1]
APrime = [7-1,2-1]
B = [1-1,6-1]
BPrime = [4-1,6-1]
gamma = 0.85
boards = stateValue(A,B,APrime, BPrime, gamma, [7,7])

print('7x7 for gamma of 0.85')
print(boards[0])
print(boards[1])

gamma = 0.75
boards = stateValue(A,B,APrime, BPrime, gamma, [7,7])

print('7x7 for gamma of 0.75')
print(boards[0])
print(boards[1])