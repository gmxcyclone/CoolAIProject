import pygame
pygame.init ()


class Button:
    def __int__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.text = text

    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.text), 0)

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman', 30)


TestButton = Button((0,250,0), 150, 225, 250, 100, 'Test')






