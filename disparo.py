import pygame
import colores

class Disparo :
    def __init__(self, x, y, imagen):
        self.imagen_disparo = pygame.image.load(imagen)
        self.rect_disparo = self.imagen_disparo.get_rect()
        self.rect_disparo.center = [x,y]
        self.velocidad_disparo = 5


    def update_disparo_jugador(self):
        self.rect_disparo.y -= self.velocidad_disparo

    def update_disparo_enemigo(self):
        self.rect_disparo.y += self.velocidad_disparo

    def dibujar_bala(self, ventana):
        ventana.blit(self.imagen_disparo,self.rect_disparo)