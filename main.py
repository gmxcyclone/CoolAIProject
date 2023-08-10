import pygame


pygame.init()
pygame.font.init()

#COLORS
BG = (0, 0, 0) #black
red = (145, 70, 70)
text = (191, 191, 191)





txtFont = pygame.font.SysFont('Times New Roman', 110)

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("GhostChat")

screen.fill(BG)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.draw.rect(screen, red,(30, 20, 580, 140), 10)
    text_title = txtFont.render("Ghost Chat", 1, text)
    screen.blit(text_title, (60, 20))



    pygame.display.flip()