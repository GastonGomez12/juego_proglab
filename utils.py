import pygame, os

pygame.init()
fuente = pygame.font.SysFont(("04b 30"), 60)

def dibujar_texto(texto, color, ventana, x, y):
    texto_obj = fuente.render(texto, 1, color)
    texto_rect = texto_obj.get_rect()
    texto_rect.center = [x,y]
    ventana.blit(texto_obj, texto_rect)

    
fuente1 = pygame.font.SysFont(("04b 30"), 20)
def dibujar_texto_en_juego(texto, color, ventana, x, y):
    texto_obj = fuente1.render(texto, 1, color)
    texto_rect = texto_obj.get_rect()
    texto_rect.center = [x,y]
    ventana.blit(texto_obj, texto_rect)