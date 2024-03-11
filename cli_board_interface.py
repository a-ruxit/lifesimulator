import random
import copy
import numpy as np

class Alive:

    def __init__(self, x, y):
        self.energy = 10
        self.foodCount = 0
        self.positionX = x
        self.positionY = y

DEAD = 0
FOOD = 1

def dead_state(width, height):
    """
    Create a basic board with all 0 values.
    :param width: <int> Width of the Board
    :param height: <int> Height of the Board
    :returns board: <lst> Dead board in the form of width x height
    """
    # return np.array([[DEAD for _ in range(height)] for _ in range(width)])
    return [[DEAD for _ in range(height)] for _ in range(width)]

def spawnFood(state, x, y):
    for i in [x-2, x-1, x, x+1, x+2]:
        for j in [y-2, y-1, y, y+1, y+2]:
            state[i][j] = FOOD

def spawnAgent(state, x ,y):
    listAgent = []
    agent = Alive(x, y)
    state[x][y] = agent
    listAgent.append(agent)
    return listAgent

def state_width(state):
    """
    Return board width
    :param state: <lst> Current State of the board
    :returns width: <int> Width of the board
    """
    return len(state)

def state_height(state):
    """
    Return board height
    :param state: <lst> Current State of the board
    :returns height: <int> Height of the board
    """
    return len(state[0])

def render(state):
    """
    Print the board in pretty form
    :param state: <lst> A random state of the board 
    :returns Nothing:
    """
    print('-'*(len(state)+2))
    for i in state:
        print('|', end='')
        for j in i:
            if j == 0:
                print(' ', end='')
            elif j == 1:
                print('#', end='')
            else:
                print('^',end='')
        print('|')
    print('-'*(len(state)+2))

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
    out_state = copy.deepcopy(state)
    pos_x = 0
    pos_y = 0
    for i in range(state_width(state)):
        for j in range(state_height(state)):
            if state[i][j] != DEAD and state[i][j] != FOOD:
                agent = out_state[i][j]
                # print(agent)
                # while True:
                x, y = agent_movement(i, j)

                if out_state[x][y] == DEAD:
                    out_state[x][y] = agent
                    out_state[i][j] = DEAD
                    pos_x = x
                    pos_y = y
                    agent.positionX = x
                    agent.positionY = y
                    agent.energy -= 2
                    print(f"Agent({agent}) moved from ({i}, {j}) to ({x}, {y}) and current energy is - {agent.energy}")

                elif out_state[x][y] == FOOD:
                    out_state[x][y] = agent
                    out_state[i][j] = DEAD
                    agent.positionX = x
                    agent.positionY = y
                    pos_x = x
                    pos_y = y
                    agent.foodCount += 1
                    agent.energy += 5
                    print(f"Agent({agent}) moved from ({i}, {j}) to ({x}, {y}) and current energy is - {agent.energy}")
    print(state[50][50])
    print(out_state[50][50])
    print(out_state[pos_x][pos_y])
    return out_state


# for i in range (1000):
#     print("\n------------------------------")
#     print(f"Iteration Number - {i}")
#     print("------------------------------\n")
#     board = dead_state(100, 100)
#     agent_list = spawnAgent(board, 50, 50)
#     next_state(board)
#     if agent_list[0].energy < 8:
#         print("\n------------------------------")
#         print(f"Error on {i}")
#         print(f"Current Energy Levels - {agent_list[0].energy}")
#         print("------------------------------\n")
#         break

board = dead_state(100, 100)
spawnFood(board, 50, 50)
agent_list = spawnAgent(board, 50, 50)
print(agent_list)
render(board)
# print(agent_list[0].energy)
next_state(board)
render(board)
# print(agent_list[0].energy)
# # print(agent_list[0].energy)