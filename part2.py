import numpy as np
import random

def calculateOptimalPolicy(initialPolicy, rewardMatrix, actions):
    # Apply the initial algo from the assignment 
    policyLen = len(initialPolicy)
    alpha = 0.001
    oldPolicy = initialPolicy
    newPolicy = [0] * policyLen
    delta = 1

    while delta > 0:
        newPolicy = [0] * policyLen
        # P(choices[i]) = policy[i]
        for i in range(policyLen):
            p2Choice = chooseAction(initialPolicy, actions)
            newPolicy[i] = oldPolicy[i] + alpha * (rewardMatrix[i,p2Choice] * (1 - oldPolicy[i]))
            for j in range(policyLen):
                if j != i:
                    newPolicy[j] = oldPolicy[j] - alpha * (rewardMatrix[j,p2Choice] * oldPolicy[j])
        delta = calculateDifference(newPolicy, oldPolicy)
        oldPolicy = newPolicy
    return newPolicy
        

def chooseAction(policy, actions):
    modifiedPolicy = [num * 100 for num in policy]
    return random.choices(actions, weights=modifiedPolicy)[0]
    
def calculateDifference(policy1, policy2):
    #finds the difference between the state values in the previous board's iteration and the current boards
    differences = []
    for i in range(len(policy1)):
        differences.append(abs(policy1[i] - policy2[i]))
    return max(differences)

def main():
    rewardBoardP1 = np.matrix([[5,0],[10,1]])
    rewardBoardP2 = rewardBoardP1.transpose()
    initPolicy = [0.5,0.5]
    choices = [0,1]

    answer = np.array(calculateOptimalPolicy(initPolicy, rewardBoardP1, choices))
    print(np.around(answer, 1))

    # rewardBoardP12 = np.matrix([[1,-1],[-1,1]])
    # rewardBoardP2 = rewardBoardP1.transpose()
    # initPolicy = [0.2,0.8]
    # choices = [0,1]

    # print(calculateOptimalPolicy([0.2,0.8], [0.2,0.8], rewardBoardP12, choices))

    # rewardBoardP12 = np.matrix([[0,-1,1], [1,0,-1], [-1,1,0]])
    # rewardBoardP2 = rewardBoardP1.transpose()
    # initPolicy = [0.6,0.2,0.2]
    # choices = [0,1,2]

    # print(calculateOptimalPolicy([0.6, 0.2, 0.2], rewardBoardP12, choices))


if __name__ == "__main__":
    main()



