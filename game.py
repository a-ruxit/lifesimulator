import pygame
import main
import time


# Environment Variables
DEAD = 0
FOOD = 1
DIED = 2

# Colors
colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0)]


pygame.init()

screen_size = 800

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('Life Simulator')


def next_state(board, agent_list):
    for j in agent_list:
        if j.energy < 0:
            board[j.positionX][j.positionY] = DIED
            j.live = False
    board = main.next_state(board)
    return board, agent_list

def render_board(board, grid_size, cell_size):
    time.sleep(1)
    for i in range(grid_size):
        for j in range(grid_size):
            if board[i][j] == DEAD:
                pygame.draw.rect(screen, colors[0], (i * cell_size, j * cell_size, cell_size, cell_size))
            elif board[i][j] == FOOD:
                pygame.draw.rect(screen, colors[2], (i * cell_size, j * cell_size, cell_size, cell_size))
            elif board[i][j] == DIED:
                pygame.draw.rect(screen, colors[3], (i * cell_size, j * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, colors[1], (i * cell_size, j * cell_size, cell_size, cell_size))

                if board[i][j].face == 1:
                    pygame.draw.circle(screen, colors[3], (i * cell_size + 2, j * cell_size + 2), 1)
                    pygame.draw.circle(screen, colors[3], (i * cell_size + 6, j * cell_size + 2), 1)
                elif board[i][j].face == 2:
                    pygame.draw.circle(screen, colors[3], (i * cell_size + 6, j * cell_size + 2), 1)
                    pygame.draw.circle(screen, colors[3], (i * cell_size + 6, j * cell_size + 6), 1)
                elif board[i][j].face == 3:
                    pygame.draw.circle(screen, colors[3], (i * cell_size + 2, j * cell_size + 6), 1)
                    pygame.draw.circle(screen, colors[3], (i * cell_size + 6, j * cell_size + 6), 1)
                elif board[i][j].face == 4:
                    pygame.draw.circle(screen, colors[3], (i * cell_size + 2, j * cell_size + 2), 1)
                    pygame.draw.circle(screen, colors[3], (i * cell_size + 2, j * cell_size + 6), 1)
                
    pygame.display.update()




run = True
while run:
    board = main.createDeadState(100, 100)
    main.spawnFood(board, 4000)
    agent_list = main.spawnAgents(board, 100)
    grid_size = len(board)
    cell_size = screen_size // grid_size
    screen.fill((0, 0, 0))
    render_board(board, grid_size, cell_size)
    time.sleep(3)
    for i in range(100):
        board, agent_list = next_state(board, agent_list)
        render_board(board, grid_size, cell_size)
    run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

# end pygame
pygame.quit()
