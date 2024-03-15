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
        self.eyeColor = self.setEyeColor()

    def setEyeColor(vision):
        if vision == 3:
            return (255, 255, 255)
        elif vision == 5:
            return (255, 255, 255)
        else:
            return (0, 0, 0)

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


def next_state(state, agent_list):
    out_state = np.copy(state)

    for agent in agent_list:
        if agent.energy < 0:
            out_state[agent.positionX][agent.positionY] = DIED
            agent.live = False
            continue

        if agent.live:
            if agent.vision == 3:
                x, y = agent.positionX, agent.positionY

                if agent.face == 1:
                    visible_cells = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
                elif agent.face == 2:
                    visible_cells = [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
                elif agent.face == 3:
                    visible_cells = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
                elif agent.face == 4:
                    visible_cells = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]
            
            if agent.vision == 5:
                x, y = agent.positionX, agent.positionY

                if agent.face == 1:
                    visible_cells = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x-1, y), (x+1, y)]
                elif agent.face == 2:
                    visible_cells = [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y-1), (x, y+1)]
                elif agent.face == 3:
                    visible_cells = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x-1, y), (x+1, y)]
                elif agent.face == 4:
                    visible_cells = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y-1), (x, y+1)]


                try:
                    agent_visible_cells = [(x, y) for x, y in visible_cells if 0 <= x < 100 and 0 <= y < 100 and state[x][y] != DIED and state[x][y] == FOOD]
                except:
                    print(agent.positionX, agent.positionY, agent.face, agent.vision, agent.energy)

                if agent_visible_cells:
                    x, y = random.choice(agent_visible_cells)
                else:
                    if ((agent.positionX == 0 and agent.face == 4) or
                        (agent.positionX == 99 and agent.face == 2) or
                        (agent.positionY == 0 and agent.face == 1) or
                        (agent.positionY == 99 and agent.face == 3)):
                        agent.face = (agent.face+2) % 4 if agent.face != 2 else 4
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


