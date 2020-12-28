import pygame as pg

class Unit(object):
    pg.init()
    _image_ = pg.image.load('images\\button.png')

    # Юнит
    def __init__(self):
        self.image = self._image_
        self.rect = self.image.get_rect()

    # Отрисовка юнмта
    def draw(self, g):
        g.blit(self.image, (self.rect.x, self.rect.y))