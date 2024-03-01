import pygame

pygame.init()

Window_Width = 900
Window_Hieght = 900

window = pygame.display.set_mode((Window_Width, Window_Hieght))

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
