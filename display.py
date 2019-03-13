import pygame
import pygame.locals

from player import Player, binput
from helpers import *
from animate import Animate

def get_textures(filename):
    m = pygame.image.load("textures/" + filename + ".png")
    mw, mh = m.get_size()
    textures = []
    for i in range(0, mh, 32):
        for j in range(0, mw, 32):
            textures.append(m.subsurface(j, i, 32, 32))
    return textures
spr = get_textures("m")

def renderp(p, s, r):
    s.fill((0,0,0))
    for i in range(p.r, p.r + 2 * r + 1):
        for j in range(p.c, p.c + 2 * r + 1):
            if -1 < i - r < p.level.r and -1 < j - r < p.level.c and p.fow[i - r][j - r]:
                if p.level.dungeon[i - r][j - r] == 0:
                    render_wall(p, i-r, j-r, s, (j - p.c) * 32, (i - p.r) * 32)
                elif p.level.dungeon[i - r][j - r] == 7:
                    s.blit(door[0], ((j - p.c) * 32, (i - p.r) * 32))
def ganimlist(p, animlist):
    for i in p.toAnim:
        for a in p.toAnim[i]:
            animlist.append(Animate(a, animdict[i], 0, 0))
    p.toAnim = {}
def ranimlist(p, s, animlist, r):
    i = 0
    while i < len(animlist):
        tmp = animlist[i].nxt()
        if tmp == None:
            animlist.pop(i)
            continue
        elif abs(animlist[i].cord[0]-p.r) <= dradius and abs(animlist[i].cord[1]-p.c) <= dradius:
            s.blit(tmp, ((animlist[i].cord[1] + dradius - p.c)*32, (animlist[i].cord[0] + dradius - p.r)*32))
        i += 1

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((672, 672))
    screen.fill((0,0,0))
    p = Player()
    dradius = 10
    playin = True
    clock = pygame.time.Clock()
    animlist = []

    
    
    while playin:
        renderp(p, screen, dradius)
                    
                    
        screen.blit(player[0], (dradius * 32, dradius * 32))
        ganimlist(p,animlist)
        ranimlist(p,screen,animlist,dradius)
        pygame.display.flip()
        clock.tick(15)
        p.cdd()
        for e in pygame.event.get():
            if e.type == pygame.locals.QUIT:
                playin = False
        pr = pygame.key.get_pressed()
        for k in (ke for ke in p.movs if pr[ke]):
                playin = binput(p, k)
        
