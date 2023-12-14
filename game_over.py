import pygame
from constantes import *
from utils import *
import colores
from base_datos import *
import re

pygame.init()


ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("GAME OVER")

# imagen_fondo = pygame.image.load("media/fondo_gameover.webp")
# imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

fondo_galaxia = pygame.image.load("media/background_h600.png")
fondo_galaxia = pygame.transform.scale(fondo_galaxia,(ANCHO_VENTANA,ALTO_VENTANA))

def game_over(score):

    running = True
    nombre = ""
    while running:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
            
                if re.match("[A-Z]", event.unicode) and len(nombre) < 3 :
                    nombre += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                
                elif event.key == pygame.K_RETURN:
                    running = False

        
        if running == False:
            insertar_puntajes(nombre, score)
        

        
        ventana.blit(fondo_galaxia,(0,0))


        dibujar_texto("Game over",colores.COLOR_BLANCO,ventana,ANCHO_VENTANA/2,150)

        dibujar_texto_en_juego("Ingrese sus iniciales [3 letras mayusculas]:",colores.COLOR_BLANCO,ventana,ANCHO_VENTANA/2,250)
        dibujar_texto_en_juego(nombre,colores.COLOR_BLANCO,ventana,ANCHO_VENTANA/2,300)

        pygame.display.flip()