import pygame

class Button:
    def __init__(self, color, hovered_color, x, y, width, height, text=''):
        self.color = color
        self.hovered_color = hovered_color  # New attribute for hovered color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.hovered_color if self.is_hovered() else self.color,
                         (self.x, self.y, self.width, self.height), 0)
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                print("Click")
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman', 30)
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            win.blit(text_surface, text_rect)

    def is_hovered(self):
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos)