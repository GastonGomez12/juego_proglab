import pygame
from enemigo import *
from constantes import *
from jugador import Jugador
from utils import *
import colores
from game_over import *
from base_datos import *
from niveles import *
from winner import *

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("MENU PRINCIPAL")
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA),0,0)
fondo_galaxia = pygame.image.load("media/fondo_nivel2.jpg")




def nivel_3(score , vidas):




    player = Jugador(ANCHO_VENTANA/2, ALTO_VENTANA-50)
    lista_enemigos = []
    enemigo_eliminado = 0

    crear_tabla_puntajes()

   
    level = 3 #defino nivel


	#evento de disparo del enemigo
    disparo_enemigo = pygame.USEREVENT + 1
    pygame.time.set_timer(disparo_enemigo, 1000)

    def dibujar_en_pantalla():
        ventana.blit(fondo_galaxia,(0,0))

        #defino los textos

        dibujar_texto_en_juego( f"Nivel : {level}", (colores.COLOR_BLANCO), ventana, 80,10)
        dibujar_texto_en_juego( f"Vidas :{vidas}", (colores.COLOR_BLANCO), ventana,ANCHO_VENTANA  - 150,10)
        dibujar_texto_en_juego( f"Score :{score}", (colores.COLOR_BLANCO), ventana, ANCHO_VENTANA/2,10)
        
		
        # dibujo los enemmigos en la ventana
        for enemigo in lista_enemigos:
            enemigo.dibujar_en(ventana)

        # dibujo la nave del jugador en la pantalla
        player.dibujar_nave(ventana)

        pygame.display.update()

    
    running = True
    while running:
        clock.tick(60)

        dibujar_en_pantalla()

        if len(lista_enemigos) == 0:
            nave_e1 = Enemigo(200, 100, "media/nave_enemiga.png",50)
            nave_e2= Enemigo(30, 160 ,"media/nave_enemiga2.png",100)
            nave_e3= Enemigo(400, 220, "media/nave_enemiga3.png",50)
            nave_e4 = Enemigo(200, 280, "media/nave_enemiga.png",50)
            nave_e5= Enemigo(30, 320, "media/nave_enemiga2.png",100)
            nave_e6= Enemigo(400,400, "media/nave_enemiga3.png",200)
            
            
            lista_enemigos.append(nave_e1)
            lista_enemigos.append(nave_e2)
            lista_enemigos.append(nave_e3)
            lista_enemigos.append(nave_e4)
            lista_enemigos.append(nave_e5)
            lista_enemigos.append(nave_e6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.disparar() #dispara el jugador
            if event.type == disparo_enemigo:
                for enemigo in lista_enemigos:
                    enemigo.disparar() #dispara el enemigo
                



        # dibujo los rectangulos y el movimiento balas del jugador
        # y las elimino en caso de que haya colision con un enemigo.
        if len(player.balas) > 0:
            for disparo in player.balas:
                disparo.dibujar_bala(ventana)
                disparo.update_disparo_jugador()

                if disparo.rect_disparo.top < -10 :
                    player.balas.remove(disparo)
                else:
                    for enemigo in lista_enemigos:
                        if disparo.rect_disparo.colliderect(enemigo.rect_enemigo):
                            explosion = pygame.mixer.Sound("media/hq-explosion-6288.mp3")
                            explosion.play()
                            explosion.set_volume(0.2)
                            player.balas.remove(disparo)
                            lista_enemigos.remove(enemigo)
                            score += enemigo.score 
                            enemigo_eliminado += 1

        if len(lista_enemigos) > 0:
                    for enemigo in lista_enemigos:
                        enemigo.update()
                        if enemigo.rect_enemigo.top > ALTO_VENTANA or enemigo.rect_enemigo.colliderect(player.rect_nave):
                            vidas -= 1
                            lista_enemigos.remove(enemigo)

                        if len(enemigo.balas) > 0:
                            for disparo in enemigo.balas:
                                disparo.dibujar_bala(ventana)
                                disparo.update_disparo_enemigo()

                                if disparo.rect_disparo.top > 900:
                                    enemigo.balas.remove(disparo)
                                elif disparo.rect_disparo.colliderect(player.rect_nave):
                                    vidas -= 1
                                    enemigo.balas.remove(disparo)
        if enemigo_eliminado == 12 :
            ganador(score)
            running = False
        elif vidas == 0 : 
            game_over(score)
            running = False

        player.update() # mueve la nave
        
        pygame.display.flip()
    
    running = False
