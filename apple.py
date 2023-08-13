import pygame as pg
from constants import SQUARE_HIGHT, SQUARE_WIDTH

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.apple = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HIGHT)

    def draw(self, screen):
        pg.draw.rect(screen, 'red', self.apple)