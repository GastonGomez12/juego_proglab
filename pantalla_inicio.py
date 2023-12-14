import pygame
from boton import Boton
import colores
from utils import *
from iniciar_juego import *
from constantes import *
from puntuacion import *

pygame.init()
pygame.mixer.init()

# Carga el archivo de audio
musica = pygame.mixer.Sound("media/neon-gaming-128925.mp3")

# Reproduce el archivo de audio en bucle
musica.play()

musica.set_volume(0.5)



def pantalla_inicio(ventana):
    dibujar_texto("SPACE WARS", (colores.COLOR_BLANCO), ventana, (ANCHO_VENTANA/2),150)

    btn_start = Boton((ANCHO_VENTANA/3), 250, "media/BOTON-START.png")
    btn_start.dibujar_en(ventana, 250, 55)

    
    btn_score = Boton((ANCHO_VENTANA/3), 350, "media/BOTON-SCORE.png")
    btn_score.dibujar_en(ventana, 250, 55)

    btn_quit = Boton((ANCHO_VENTANA/3), 450, "media/BOTON-EXIT.png")
    btn_quit.dibujar_en(ventana, 250, 55)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_start.es_presionado():
                musica.stop()
                iniciar_juego()
            elif btn_score.es_presionado():
                puntajes()
            elif btn_quit.es_presionado():
                exit()