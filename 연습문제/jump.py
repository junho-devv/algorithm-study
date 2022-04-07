import pygame
import sys

pygame.init()

screenSize = (400, 300)
gameScreen = pygame.display.set_mode(screenSize)

gameloopCount = 0
running = True

while running:
    for event in pygame.event.get():
        gameloopCount += 1
        print(gameloopCount, " : ", event)
        if event.type == pygame.QUIT:
            running = False
        pygame.draw.rect(gameScreen, (0,125,255), pygame.Rect(0,0,100,100))
        pygame.display.flip()

pygame.quit()
sys.exit()