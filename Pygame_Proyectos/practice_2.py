import pygame


pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("TEST")
running = True

imagen = pygame.image.load("car.png")
imagen = pygame.transform.scale(imagen,(150,150))
rect_objeto = pygame.Rect(300,400,40,40)
# imagen_colision = pygame.image.load("mosca.png")
# imagen_colision = pygame.transform.scale(imagen_colision,(50,50))
# rect_colision = imagen_colision.get_rect()



while running:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            running = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            posicionClick = list(evento.pos)
            rect_objeto[0] = posicionClick[0]
            rect_objeto[1] = posicionClick[1]

    screen.fill((0,134,0))


    pygame.draw.rect(screen,(255,255,255),rect_objeto)
    screen.blit(imagen,rect_objeto)
    pygame.display.flip()
    