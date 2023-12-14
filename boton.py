import pygame, os

class Boton():
	def __init__(self, x, y, img_name):
		self.x = x
		self.y = y
		self.imagen = pygame.image.load((img_name))
		self.rect_boton = pygame.Rect((self.x,self.y),(300,60))

	def dibujar_en(self, ventana, scale_width, scale_height):
		img = pygame.transform.scale(self.imagen, (scale_width, scale_height))
		ventana.blit(img, self.rect_boton)

	def es_presionado(self):
		if self.rect_boton.collidepoint(pygame.mouse.get_pos()):
			return True
		else:
			return False
	