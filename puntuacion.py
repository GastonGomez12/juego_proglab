import pygame
from utils import *
import colores
from base_datos import *
from constantes import *

pygame.init()

 
clock = pygame.time.Clock()


pygame.display.set_caption("PUNTAJES")
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

fondo_galaxia = pygame.image.load("media/background_h600.png")
fondo_galaxia = pygame.transform.scale(fondo_galaxia,(ANCHO_VENTANA,ALTO_VENTANA))

def puntajes():

    puntajes = obtener_datos()

        
    fuente = pygame.font.SysFont(("04b 30"), 20)

    running = True

    while running:
        
        ventana.blit(fondo_galaxia,(0,0))
        dibujar_texto_en_juego("PUNTAJES MAXIMOS", (colores.COLOR_BLANCO), ventana,(ANCHO_VENTANA/2),50)

        for i, valor in enumerate(puntajes):
            texto = fuente.render(f"{valor[1]}     {valor[2]}", True, (colores.COLOR_BLANCO))
            rect_texto = texto.get_rect()
            rect_texto.center = (ANCHO_VENTANA/2, 250 + i * 50)
            ventana.blit(texto, rect_texto)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)