import pygame
pygame.init()
font = pygame.font.Font('freesanbold.ttf', 24)

message = 'greetings mortal, how are you today?'

snip = font.render('', True, 'white')
counter = 0
speed = 3
done = False