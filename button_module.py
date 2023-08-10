import pygame

pygame.init()


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] and not self.clicked:
                    selfe.clicked = True
                    print("Click")
                if not pygame.mouse.get_pressed()[0]:
                    self.clicked = False

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman', 30)
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            win.blit(text_surface, text_rect)
