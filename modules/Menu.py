import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['start', 'create', 'load', 'save', 'options', 'about the game', 'return', 'exit']

    def __init__(self):
        """Отрисовка меню"""
        self.list_button = [8]
        for i in range(8):
            button = Button(375, 100, self.button_name[i])
            self.list_button.add(button)

    def update(self, e):
        """Отрисовка меню"""
        pass

    # Отрисовка меню
    def draw(self, g):
        """Отрисовка меню"""
        g.fill('blue')
        self.button.draw(g)
        for i in range(8):
            button = Button(375, 100, self.button_name[i])