import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 600, 400
TAM_BLOQUE = 20
FPS = 10

NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake")
reloj = pygame.time.Clock()

snake = [(100, 100), (80, 100), (60, 100)]
direccion = (TAM_BLOQUE, 0)

def nueva_comida():
    while True:
        pos = (random.randrange(0, ANCHO, TAM_BLOQUE), random.randrange(0, ALTO, TAM_BLOQUE))
        if pos not in snake:
            return pos

comida = nueva_comida()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direccion != (0, TAM_BLOQUE):
                direccion = (0, -TAM_BLOQUE)
            elif event.key == pygame.K_DOWN and direccion != (0, -TAM_BLOQUE):
                direccion = (0, TAM_BLOQUE)
            elif event.key == pygame.K_LEFT and direccion != (TAM_BLOQUE, 0):
                direccion = (-TAM_BLOQUE, 0)
            elif event.key == pygame.K_RIGHT and direccion != (-TAM_BLOQUE, 0):
                direccion = (TAM_BLOQUE, 0)

    cabeza = (snake[0][0] + direccion[0], snake[0][1] + direccion[1])

    if (cabeza[0] < 0 or cabeza[0] >= ANCHO or
        cabeza[1] < 0 or cabeza[1] >= ALTO or
        cabeza in snake):
        break

    snake.insert(0, cabeza)

    if cabeza == comida:
        comida = nueva_comida()
    else:
        snake.pop()

    pantalla.fill(NEGRO)
    for pos in snake:
        pygame.draw.rect(pantalla, VERDE, (*pos, TAM_BLOQUE, TAM_BLOQUE))
    pygame.draw.rect(pantalla, ROJO, (*comida, TAM_BLOQUE, TAM_BLOQUE))

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()