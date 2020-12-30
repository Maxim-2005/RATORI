import pygame as pg
from modules.Unit import Unit

class Game(object):

    # ИГРА
    def __init__(self):
        self.unit = Unit()

    # Обновление
    def update(self, e):
        if e.type == pg.KEYDOWN and e.key == pg.K_UP:
            self.unit.rect.y -= 10
        if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            self.unit.rect.y += 10
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            self.unit.rect.x -= 10
        if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            self.unit.rect.x += 10

    # Отрисовка игры
    def draw(self, g):
        g.fill('grey')
        self.unit.draw(g)