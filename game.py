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


def draw_screen():
    board = main.createDeadState(100, 100)
    main.spawnFood(board, 4000)
    agent_list = main.spawnAgents(board, 100)
    grid_size = len(board)
    cell_size = screen_size // grid_size
    screen.fill((0, 0, 0))
    draw_board_assets(board, grid_size, cell_size)
    for i in range(300):
        if i % 20 == 0:
            for j in agent_list:
                if j.energy < 5:
                    board[j.positionX][j.positionY] = DIED
                    j.live = False
        board = main.next_state(board)
        draw_board_assets(board, grid_size, cell_size)
    return board, agent_list

def draw_board_assets(board, grid_size, cell_size):
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
    pygame.display.update()


run = True
while run:
    board, agent_list = draw_screen()

    count = 0
    for i in agent_list:
        if i.live == False:
            count += 1
    if count == len(agent_list):
        run = False
    print(count)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

# end pygame
pygame.quit()
