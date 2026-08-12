import pygame
import random
import sys

pygame.init()

# fix estable
PYGAME_DETECT_AVX2=1


ANCHO, ALTO = 600, 400
TAM_BLOQUE = 20
FPS = 10

NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake")
reloj = pygame.time.Clock()


def nueva_comida(snake):
    while True:
        pos = (random.randrange(0, ANCHO, TAM_BLOQUE), random.randrange(0, ALTO, TAM_BLOQUE))
        if pos not in snake:
            return pos


font_large = pygame.font.SysFont(None, 72)
font_small = pygame.font.SysFont(None, 36)


def draw_text(surface, text, font, color, center):
    img = font.render(text, True, color)
    rect = img.get_rect(center=center)
    surface.blit(img, rect)
    return rect


def game_over_screen():
    retry_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 20, 200, 50)
    quit_rect = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 90, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if retry_rect.collidepoint(event.pos):
                    return True
                if quit_rect.collidepoint(event.pos):
                    return False

        pantalla.fill(NEGRO)
        draw_text(pantalla, "Game Over", font_large, ROJO, (ANCHO // 2, ALTO // 2 - 40))
        pygame.draw.rect(pantalla, VERDE, retry_rect)
        pygame.draw.rect(pantalla, ROJO, quit_rect)
        draw_text(pantalla, "Retry (R)", font_small, NEGRO, retry_rect.center)
        draw_text(pantalla, "Quit (Q)", font_small, NEGRO, quit_rect.center)

        pygame.display.flip()
        reloj.tick(30)


def run_game():
    snake = [(100, 100), (80, 100), (60, 100)]
    direccion = (TAM_BLOQUE, 0)
    comida = nueva_comida(snake)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
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
            return game_over_screen()

        snake.insert(0, cabeza)

        if cabeza == comida:
            comida = nueva_comida(snake)
        else:
            snake.pop()

        pantalla.fill(NEGRO)
        for pos in snake:
            pygame.draw.rect(pantalla, VERDE, (*pos, TAM_BLOQUE, TAM_BLOQUE))
        pygame.draw.rect(pantalla, ROJO, (*comida, TAM_BLOQUE, TAM_BLOQUE))

        pygame.display.flip()
        reloj.tick(FPS)


def main():
    # permitir volver a intentar
    while True:
        retry = run_game()
        if not retry:
            break


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
        sys.exit()