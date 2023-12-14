import pygame, os, random
from constantes import *
from disparo import *

class Enemigo:
    def __init__(self,x,y, imagen,score) -> None:
        self.imagen_enemigo = pygame.image.load(imagen)
        self.rect_enemigo = self.imagen_enemigo.get_rect()
        self.rect_enemigo.center = [x,y]
        self.balas = []
        self.velocidad = random.randrange(2, 5, 1)
        self.direction = 'der'
        self.score = score
        


    def update_dir(self, new_dir):
        self.direction = new_dir

    def update(self):
        if self.rect_enemigo.right >= ANCHO_VENTANA:
            self.update_dir("izq")
        if self.rect_enemigo.left <= 10:
            self.update_dir("der")
        
        if self.direction == "der":
            self.rect_enemigo.x += self.velocidad
        else:
            self.rect_enemigo.x -= self.velocidad

    def disparar(self):
        bala = Disparo(self.rect_enemigo.centerx,self.rect_enemigo.centery,"media/disparo_enemigo.png")
        self.balas.append(bala)


    def dibujar_en(self, ventana):
        ventana.blit(self.imagen_enemigo, self.rect_enemigo)


