import numpy as np
import random
import pygame

class Alive:

    def __init__(self, x, y):
        self.live = True
        self.energy = 10
        self.face = random.choice([1, 2, 3, 4])
        self.vision = random.choices([0, 3, 5], weights=[10, 1, 0.1], k=1)[0]
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

def agent_movement(vision, face, X, Y):
    """
    Creates new coordinates for the Agent's Position
    :param X, Y: <int> Coordinate's of the current position of the Agent
    :returns x, y: <int> Coordinate's of new position of the Agent
    """

    if vision == 3:
        if face == 1:
            pass


    x, y = random.choice([X-1, X, X+1]), random.choice([Y-1, Y, Y+1])
    if x < 0:
        x = 0
    elif x > 99:
        x = 99
    if y < 0:
        y = 0
    elif y > 99:
        y = 99
    return x, y

def next_state(state, agent_list):
    """
    Creates the next state of the board after Agents have moved
    :param state: <lst> Current state of the board
    :returns out_state: <lst> State of the board after movement 
    """
    out_state = np.copy(state)

    for agent in agent_list:
        if agent.energy < 0:
            out_state[agent.positionX][agent.positionY] = DIED
            agent.live = False
            continue

        if agent.live:
            if agent.vision == 3:
                visible_cells = []
                x, y = agent.positionX, agent.positionY

                if agent.face == 1:
                    visible_cells = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
                elif agent.face == 2:
                    visible_cells = [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
                elif agent.face == 3:
                    visible_cells = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
                elif agent.face == 4:
                    visible_cells = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]

                visible_cells = [(x, y) for x, y in visible_cells if 0 <= x < 100 and 0 <= y < 100 and state[x][y] != DIED]

                if visible_cells:
                    x, y = random.choice(visible_cells)
                else:
                    x, y = random.choice([(agent.positionX + dx, agent.positionY + dy) for dx in range(-1, 2) for dy in range(-1, 2)])
                    x = min(max(x, 0), 99)
                    y = min(max(y, 0), 99)

            else:
                x, y = random.choice([(agent.positionX + dx, agent.positionY + dy) for dx in range(-1, 2) for dy in range(-1, 2)])
                x = min(max(x, 0), 99)
                y = min(max(y, 0), 99)

            if out_state[x][y] == DEAD:
                out_state[x][y] = agent
                out_state[agent.positionX][agent.positionY] = DEAD
                agent.positionX, agent.positionY = x, y
                agent.energy -= 2
            elif out_state[x][y] == FOOD:
                out_state[x][y] = agent
                out_state[agent.positionX][agent.positionY] = DEAD
                agent.positionX, agent.positionY = x, y
                agent.energy += 3

    return out_state


