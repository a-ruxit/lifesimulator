# Importing the library
import pygame
 
# Initializing Pygame
pygame.init()
 
# Initializing surface
surface = pygame.display.set_mode((800,800))
 
# Initializing Color
color = (255,0,0)
color2 = (0,255,0)
 
i, j = 50, 50
cell_size = 8
 
# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(i * cell_size, j * cell_size, cell_size, cell_size))
pygame.draw.circle(surface, color2, (i * cell_size + 6, j * cell_size + 2), 1)
pygame.draw.circle(surface, color2, (i * cell_size + 6, j * cell_size + 6), 1)
pygame.display.flip()


run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

# end pygame
pygame.quit()
