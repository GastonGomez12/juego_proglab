import pygame
from pantalla_inicio import *
from constantes import *

pygame.init() 

clock = pygame.time.Clock()

pygame.display.set_caption("MENU PRINCIPAL")
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA),0,0)

# fondo_galaxia = pygame.image.load("media/background_h600.png")
# fondo_galaxia = pygame.transform.scale(fondo_galaxia,(ANCHO_VENTANA,ALTO_VENTANA))

imagen_fondo = pygame.image.load("media/fondo_gameover.webp")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

def main():
    running = True
    while running:
        clock.tick(60)
        ventana.blit(imagen_fondo,(0,0))

        pantalla_inicio(ventana)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        pygame.display.flip()
    
    pygame.quit()

main()