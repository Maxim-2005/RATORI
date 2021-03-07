import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['start', 'create', 'load', 'save', 'options', 'about the game', 'return', 'exit']

    def __init__(self):
        """Отрисовка меню"""
        self.list_button = []
        for i in range(8):
            if i < 4:
                pos_x = 345
                pos_y = i*110+150
            else:
                pos_x = 655
                pos_y = i*110-290
            button = Button(pos_x, pos_y, self.button_name[i])
            self.list_button.append(button)
        self.button_action = None
        self.list_button[6].active = False

    def update(self, e):
        """Отрисовка меню"""
        if e.type == pg.MOUSEMOTION:
            self.button_action = None
        pos = pg.mouse.get_pos()
        click = pg.mouse.get_pressed(3)
        for button in self.list_button:
            if button.active and button.rect.collidepoint(pos):
                button.focus = True
                if click[0]:
                    button.pressed = True
                    self.functions(button.name)
                else:
                    button.pressed = False
            else:
                button.focus = False
            button.update()

    # Отрисовка меню
    def draw(self, g):
        """Отрисовка меню"""
        g.fill('black')
        for button in self.list_button:
            button.draw(g)

    def function(self, button_name):
        pass