import pygame
from constantes import *
from disparo import *

class Jugador:

    def __init__(self,x,y) -> None:
        self.imagen_nave = pygame.image.load("media/nave.png")
        self.rect_nave = self.imagen_nave.get_rect()
        self.rect_nave.center = [x,y]
        self.balas = []
        # Velocidad inicial del personaje
        self.velocidad_x = 5
        self.sonido_disparo =  pygame.mixer.Sound("media/laser-zap-90575.mp3")
    
    def update (self):
        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        
        if teclas[pygame.K_a] and self.rect_nave.left > 0:
            self.rect_nave.x -= self.velocidad_x
        if teclas[pygame.K_d] and self.rect_nave.right < ANCHO_VENTANA:
            self.rect_nave.x += self.velocidad_x


    def disparar (self):
        dispara = Disparo(self.rect_nave.centerx,self.rect_nave.top,"media/disparo.png")
        self.balas.append(dispara)
        self.sonido_disparo.play()
        self.sonido_disparo.set_volume(0.2)
    
        
    def dibujar_nave(self,ventana):
        ventana.blit(self.imagen_nave,self.rect_nave)
        for disparo in self.balas:
            disparo.dibujar_bala(ventana)