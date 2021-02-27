import pygame as pg
import pygame

class Button(object):
    pg.init()
    pg.font.init()
    _font_ = pg.font.SysFont('cambria', 30)

    def __init__(self, pos_x, pos_y, name):
        """Конструктор кнопки"""
        self.name = name
        self.active = True
        self.focus = False
        self.pressed = False
        self.rect = pg.Rect(pos_x, pos_y, 375, 100)

    def draw(self, g):
        """Отрисовка кнопки"""
        pg.draw.rect(g, 'white', self.rect, 5)
        self.text_button = self._font_.render(self.name, True, 'red')
        self.text_rect = self.text_button.get_rect()
        self.text_rect.center = self.rect.center
        g.blit(self.text_button, self.text_rect)

