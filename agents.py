import random

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
    return [[DEAD for _ in range(height)] for _ in range(width)]

def spawnFood():
    pass

def spawnAgent():
    pass

def random_state(width, height):
    """
    Creates a board with random state values
    :param width: <int> Width of the Board
    :param height: <int> Height of the Board
    :returns board: <lst> Random state board in the form of width x height
    """
    # Create a dead board
    state = dead_state(width, height)
    out_state = []
    cells = []
    for i in range(state_width(state)):
        if i != 0 and i != state_width(state)-1:
            for j in range(state_height(state)):
                if j != 0 and j != state_height(state)-1:
                    random_num = random.random()
                    if random_num >= 0.99:
                        cell_state = FOOD
                    else:
                        cell_state = DEAD
                    state[i][j] = cell_state
            out_state.append(state[i])
        else:
            for j in range(state_height(state)):
                # This will create agents on random rate
                # random_num = random.random()
                # if random_num >= 0.9:
                #     agent = Alive(i, j)
                #     cell_state = agent
                #     cells.append(agent)
                # else:
                #     cell_state = DEAD
                # state[i][j] = cell_state

                # This will create agents on all positions in first and last row
                agent = Alive(i, j)
                cell_state = agent
                cells.append(agent)
                state[i][j] = cell_state
            out_state.append(state[i])
    return state, cells

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

def next_state(state):
    """
    Creates the next state of the board after Agents have moved
    :param state: <lst> Current state of the board
    :returns out_state: <lst> State of the board after movement 
    """
    out_state = state
    for i in range(state_width(state)):
        for j in range(state_height(state)):
            if state[i][j] != DEAD and state[i][j] != FOOD:
                agent = state[i][j]
                while True:
                    x, y = agent_movement(i, j)

                    if out_state[x][y] == DEAD:
                        out_state[x][y] = agent
                        out_state[i][j] = DEAD
                        agent.positionX = x
                        agent.positionY = y
                        agent.energy -= 2

                    elif out_state[x][y] == FOOD:
                        out_state[x][y] = agent
                        out_state[i][j] = DEAD
                        agent.positionX = x
                        agent.positionY = y
                        agent.foodCount += 1
                        agent.energy += 5

                    break
    return out_state

def life_count(state):
    """
    Gives the life count of the board
    :param state: <lst> Current state of the board
    :returns count: <int> Number of alive cells on the board
    """
    count = 0
    for i in range(state_width(state)):
        for j in range(state_height(state)):
            if state[i][j] != DEAD and state[i][j] != FOOD:
                count += 1
    return count

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


board, livingAgents = random_state(100, 100)

for i in range(10):
    print("Life count of the board = ", life_count(board))
    render(board)
    next_state(board)
print("Life count of the board = ", life_count(board))
# render(board)
# print(board)
# print(livingAgents)

for i in livingAgents:
    if i.energy > 0:
        print(i, i.energy)