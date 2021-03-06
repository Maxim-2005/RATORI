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

    def update(self, e):
        """Отрисовка меню"""
        pass

    # Отрисовка меню
    def draw(self, g):
        """Отрисовка меню"""
        g.fill('black')
        for button in self.list_button:
            button.draw(g)