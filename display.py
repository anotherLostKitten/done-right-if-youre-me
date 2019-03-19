import pygame
import pygame.locals
from math import floor
from m import *
def get_textures(filename):
    m = pygame.image.load(filename + ".png")
    mw, mh = m.get_size()
    textures = []
    for i in range(0, mh, 32):
        for j in range(0, mw, 32):
            textures.append(m.subsurface(j, i, 32, 32))
    return textures
spr = get_textures("m")

def renderp(s, b):
    s.fill((0,0,0))
    for i in range(b.r):
        for j in range(b.c):
            t = b.b[i*b.c+j]
            if b.v[i*b.c+j]!=1:
                s.blit((spr[t] if t >= 0 else spr[23]) if b.v[i*b.c+j]==0 else spr[10],(j*32,i*32))
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((32*30, 32*16))
    screen.fill((0,0,0))
    playin = True
    clock = pygame.time.Clock()
    b=B(16,30,99)
    while playin:
        renderp(screen,b)
        pygame.display.flip()
        clock.tick(15)
        for e in pygame.event.get():
            if e.type == pygame.locals.QUIT:
                playin = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                xy=[floor(i/32)for i in pygame.mouse.get_pos()]
                t = e.button
                if t==1 or t==3:
                    b.clk(xy[1],xy[0],t==1)
