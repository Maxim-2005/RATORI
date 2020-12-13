import pygame

local_version = 1

pygame.init()
g = pygame.display.set_mode((800, 600))
pygame.display.set_caption('RATORI')
icon = pygame.image.load('images\\icon.ico')
image = pygame.image.load('images\\BG.png')
pygame.display.set_icon(icon)
game_state = True
def game_cycle():
    while game_state:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        g.fill('brown')
        #pygame.draw.line(g, 'yellow', (50, 50), (500, 100), 1)
        #pygame.draw.aaline(g, 'yellow', (50, 150), (500, 200), 1)
        #pygame.draw.line(g, 'red', (250, 50), (300, 200), 1)

        #pygame.draw.rect(g, 'black', (100, 100, 300, 300), 5)
        #pygame.draw.circle(g, 'white', (400, 400), 100, 5)
        #pygame.draw.ellipse(g, 'purple', (500, 300, 200, 100), 5)
        #pygame.draw.arc(g, 'orange', (300, 200, 400, 250), 6, 3, 3)

        #g.blit(image, (125, 325))

        pygame.draw.line(g, (139, 69, 19), (400, 125), (400, 500), 30)
        pygame.draw.rect(g, 'darkgreen', (300, 350, 200, 100))
        pygame.draw.rect(g, 'darkgreen', (325, 250, 150, 100))
        pygame.draw.rect(g, 'darkgreen', (350, 150, 100, 100))
        pygame.draw.rect(g, 'darkgreen', (375, 100, 50, 50))

        pygame.time.Clock().tick(60)
        pygame.display.update()