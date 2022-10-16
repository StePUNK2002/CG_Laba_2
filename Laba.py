import pygame
import os

WHITE = (255, 255, 255)

# ----------  чтобы окно появлялось в верхнем левом углу ------------
x = 20
y = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
# --------------------------------------------------------------------

pygame.init()

W = 1000
H = 600

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Множества Жюлиа")
sc.fill(WHITE)

FPS = 60        # число кадров в секунду
clock = pygame.time.Clock()


c = complex(0.32, -0.043)
P = 495                     # размер [2*P+1 x 2*P+1]
scale = P / 3.1              # масштабный коэффициент
view = (00, 210)            # координаты смещения угла обзора
n_iter = 100                # число итераций для проверки принадлежности к множеству Жюлиа

for y in range(-P+view[1], P+view[1]):
    for x in range(-P+view[0], P+view[0]):
        a = x / scale
        b = y / scale
        z = complex(a, b)
        n = 0
        for n in range(n_iter):
            z = z**2 + c
            if abs(z) > 2:
                break

        if n == n_iter-1:
            r = g = b = 0
        else:
            r = (n % 2) * 32
            g = (n % 4) * 64
            b = (n % 2) * 16 + 128
            r = g = b = 250

        pygame.draw.circle(sc, (r, g, b), (x + P - view[0], y + P - view[1]), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(FPS)