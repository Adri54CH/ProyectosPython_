import pygame
from random import randint
pygame.init()

screen = pygame.display.set_mode((500,500))
running = True
pygame.display.set_caption("cols")
velocidad = 20
direccion = True #Controla la direccion del rectangulo -true derecha
# -false izquierda 
posX,posY = randint(1,400), randint(1,300) #Asigna una posicion random para x,y 
while running:

    screen.fill((120,120,120))

    rectangulo = pygame.Rect((posX,posY,50,50))
    rectangulo2 = pygame.draw.rect(screen,(0,0,0),rectangulo)

        
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            x,y = event.pos
            print(x,y)

        """if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posX -= velocidad
                if posX < 0:
                    posX = 0
            elif event.key == pygame.K_RIGHT:
                posX += velocidad
                if posX > 500 - 50:
                    posX = 500 - 50"""

    pygame.display.flip()


pygame.quit()