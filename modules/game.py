import pygame
from modules.Class1 import class1

local_version = 1

pygame.init()
g = pygame.display.set_mode((800, 600))
icon = pygame.image.load('images\\icon.png')
pygame.display.set_caption('RATORI')
game_music = pygame.mixer.music.load('sounds\\audio.mp3')
sound = pygame.mixer.Sound('sounds\\sound.wav')
image = pygame.image.load('images\\BG.png')
pygame.display.set_icon(icon)
font = pygame.font.SysFont('serif', 32)
msg = 'Hello World'
text = font.render(msg, True, 'grey')
game_state = True
class1 = class1()

def game_cycle():
    pygame.mixer.music.play(-1)
    pygame.mixer.Sound.play(sound)
    while game_state:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        class1.draw(g)
        g.blit(image, (125, 325))
        g.blit(text, (300, 50))

        pygame.time.Clock().tick(60)
        pygame.display.update()