import pygame

from button_module import Button
from pygame import mixer

pygame.init()
pygame.font.init()

# window
screen_width = 640
screen_height = 480

# COLORS
BG = (0, 0, 0)  # black
red = (145, 70, 70)
text = (191, 191, 191)

# START BUTTON
startButton = Button((145, 70, 70), (50, 0, 0), 250, 200, 150, 50, "Begin Séance")

# background
startBackground = pygame.image.load('assets/background.jpg')


def draw_startBackground():
    screen.blit(startBackground, (0, 0))


# background Sound
mixer = pygame.mixer
mixer.music.load('assets/forShet.mp3')
mixer.music.play(-1)
mixer.music.play()


# title
def draw_title():
    pygame.draw.rect(screen, red, (30, 20, 580, 140), 10)
    text_title = txtFont.render("Ghost Chat", 1, text)
    screen.blit(text_title, (60, 20))


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

    draw_startBackground()
    draw_title()
    startButton.draw(screen)

    pygame.display.flip()
