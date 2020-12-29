import pygame as pg
from modules.Unit import Unit

class Game(object):

    # ИГРА
    def __init__(self):
        self.unit = Unit()
        self.unit.

    # Отрисовка игры
    def draw(self, g):
        g.fill('grey')
        self.unit.draw(g)