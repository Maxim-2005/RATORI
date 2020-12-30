import pygame as pg

class Button(object):
    pg.init()
    _image_ = pg.image.load('images\\BG.png')

    # Кнопка
    def __init__(self):
        self.image = self._image_
        self.rect = self.image.get_rect()

    # Отрисовка кнопки
    def draw(self, g):
        g.blit(self.image, self.rect)