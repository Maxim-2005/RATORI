#RATORI-game
from modules import game

current_version = 1 #Запрос версии с интернета

if __name__ == '__main__':
    local_version = game.local_version
    if local_version < current_version:
        print("Вышла новая версия")
    else:
        game.game_cycle()