
import pygame
from random import randint
pygame.init()

screen = pygame.display.set_mode((500,500))
running = True
pygame.display.set_caption("cols")
velocidad = 20
print(velocidad) 
#direccion = True #Controla la direccion del rectangulo -true derecha
# -false izquierda 
#posX,posY = randint(1,400), randint(1,300) #Asigna una posicion random para x,y 
while running:

    screen.fill((120,120,120))

 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            x,y = event.pos
            print(x,y)



    pygame.display.flip()


pygame.quit()