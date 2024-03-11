import numpy as np
import random
import pygame

class Alive:

    def __init__(self, x, y):
        self.live = True
        self.energy = 10
        self.foodCount = 0
        self.positionX = x
        self.positionY = y

DEAD = 0
FOOD = 1
DIED = 2

def createDeadState(xdims, ydims):
    return np.array([[DEAD for _ in range(ydims)] for _ in range(xdims)], dtype=object)

def state_width(state):
    """
    Return board width
    :param state: <lst> Current State of the board
    :returns width: <int> Width of the board
    """
    return len(state)

def spawnAgents(state, num):
    listAgent = []
    for i in range (num):
        while True:
            x = random.randrange(100)
            y = random.randrange(100)
            if state[x][y] == DEAD:
                agent = Alive(x, y)
                state[x][y] = agent
                listAgent.append(agent)
                break
    return listAgent

def spawnFood(state, num):
    for i in range(num):
        while True:
            x = random.randrange(100)
            y = random.randrange(100)
            if state[x][y] == DEAD:
                state[x][y] = FOOD
                break

def state_height(state):
    """
    Return board height
    :param state: <lst> Current State of the board
    :returns height: <int> Height of the board
    """
    return len(state[0])

def agent_movement(X, Y):
    """
    Creates new coordinates for the Agent's Position
    :param X, Y: <int> Coordinate's of the current position of the Agent
    :returns x, y: <int> Coordinate's of new position of the Agent
    """
    x, y = random.choice([X-2, X-1, X, X+1, X+2]), random.choice([Y-2, Y-1, Y, Y+1, Y+2])
    if x < 0:
        x = 0
    elif x > 99:
        x = 99
    if y < 0:
        y = 0
    elif y > 99:
        y = 99
    return x, y

def next_state(state):
    """
    Creates the next state of the board after Agents have moved
    :param state: <lst> Current state of the board
    :returns out_state: <lst> State of the board after movement 
    """
    out_state = np.copy(state)
    pos_x = 0
    pos_y = 0
    for i in range(state_width(state)):
        for j in range(state_height(state)):
            if state[i][j] != DEAD and state[i][j] != FOOD and state[i][j] != DIED:
                agent = out_state[i][j]
                x, y = agent_movement(i, j)

                if out_state[x][y] == DEAD:
                    out_state[x][y] = agent
                    out_state[i][j] = DEAD
                    pos_x = x
                    pos_y = y
                    agent.positionX = x
                    agent.positionY = y
                    agent.energy -= 2

                elif out_state[x][y] == FOOD:
                    out_state[x][y] = agent
                    out_state[i][j] = DEAD
                    agent.positionX = x
                    agent.positionY = y
                    pos_x = x
                    pos_y = y
                    agent.foodCount += 1
                    agent.energy += 3
    return out_state

