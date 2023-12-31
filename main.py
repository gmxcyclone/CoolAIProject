import pygame

from button_module import Button
from pygame import mixer

pygame.init()
pygame.font.init()
timer = pygame.time.Clock()

# window
screen_width = 640
screen_height = 480

# COLORS
BG = (0, 0, 0)  # black
red = (145, 70, 70)
text = (191, 191, 191)

# START BUTTON
startButton = Button((145, 70, 70), (50, 0, 0), 120, 200, 175, 50, "Begin Séance")
exitButton = Button((145, 70, 70), (50, 0, 0), 345, 200, 175, 50, "Exit Game")

# background
startBackground = pygame.image.load('assets/background.jpg')


# text speed
boxFont = pygame.font.SysFont('Times New Roman', 24)
timer = pygame.time.Clock()
message = 'Daniyal is a stinky panchout who likes men'
snip = boxFont.render('', True, 'white')
counter = 0
speed = 3
done = False


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

spriteSheet = pygame.image.load('assets/sprite.png')


def get_image(sheet, frame, width, height, scale):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image


animation_list = []
animation_talk = 3
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0
idleCount = 1
isTalking = False

animation_list = []
animation_talk = 3

for x in range(animation_talk):
    animation_list.append(get_image(spriteSheet, x, 82, 118, 2.5))



#ANIMATIONS

pos = {
    0: (200, 40),
    1: (210, 40),
    2: (220, 40),
    3: (210, 40)
}
def idle(frame):

    x_pos, y_pos = pos[frame]
    screen.blit(animation_list[1], (x_pos, y_pos))

def talking(frame):
    screen.blit(animation_list[frame], (210, 40))



# SCREEN SELECT
main = 0
game = 1
current = main

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BG)

    if current == main:
        draw_startBackground()
        draw_title()
        startButton.draw(screen)
        exitButton.draw(screen)

        if startButton.clicked:
            current = game
        if exitButton.clicked:
            pygame.quit()

    elif current == game:
        screen.fill(BG)

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1

            last_update = current_time;
            if frame >= len(animation_list) + 1:
                frame = 0

        if isTalking == False:
            if frame >= len(animation_list) + 1:
                frame = 0
            idle(frame)

        elif isTalking == True:
            if frame >= len(animation_list) - 1:
                frame = 0
            talking(frame)

        timer.tick(60)
        pygame.draw.rect(screen, (184, 134, 11), [0, 350, 700, 200])
        pygame.draw.rect(screen, (139, 69, 19), [0, 350, 640, 200], 10)

        if counter < speed *len(message):
            isTalking = True
            counter += 1
        elif counter >= speed*len(message):
            done = True
            isTalking = False

        snip = boxFont.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (20, 360))

    pygame.display.flip()
