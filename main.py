#RATORI-game
from modules import game
from pyautogui import *

current_version = 2 #Запрос версии с интернета
window_name = 'update'
window_text = 'Вышла новая версия игры RaToRi'

if __name__ == '__main__':
    local_version = game.local_version
    if local_version < current_version:
        print(window_text)
        alert(window_text, window_name, button='OK')
    else:
        game.game_cycle()