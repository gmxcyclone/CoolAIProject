import pygame


pygame.init()

#COLORS
BG = (0, 0, 0) #black

screen = pygame.display.set_mode((400, 500))

pygame.display.set_caption("CoolAIProject")

screen.fill(BG)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BG)
    pygame.display.flip()
