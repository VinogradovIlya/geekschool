import pygame
import hero
import pacman
import random
import time
import os
from pathlib import Path
pygame.init()


DIR = Path(__file__).resolve().parent
os.chdir(DIR)
BACK = (90, 2, 166)
WINDOW_W = 700
WINDOW_H = 700

mw = pygame.display.set_mode((WINDOW_W, WINDOW_H))
mw.fill(BACK)
clock = pygame.time.Clock()

enemies = pygame.sprite.Group()
for i in range(4):
    x = random.randint(50, WINDOW_W-50)
    y = random.randint(50, WINDOW_H-50)
    enemies.add(hero.Hero('ghost.png', x, y, 50, 50, 5))

player = pacman.Pacman('pacman3.png', WINDOW_W/2, WINDOW_H/2, 50, 50, 10)

running = True
start = time.time()
for e in enemies:
    e.direct()
while running:
    now = time.time()
    if now - start >= 5:
        for e in enemies:
            e.direct()
        start = now
    for e in enemies:
        e.move(e.direction)
        e.outside(WINDOW_W, WINDOW_H)
    mw.fill(BACK)
    enemies.draw(mw)
    player.outside(WINDOW_W, WINDOW_H)
    player.reset(mw)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        player.move(e)
    if player.up:
        player.move_up()
    if player.down:
        player.move_down()
    if player.left:
        player.move_left()
    if player.right:
        player.move_right()
    player.outside(WINDOW_W, WINDOW_H)

    pygame.sprite.spritecollide(player, enemies, True)
    if not len(enemies):
        for i in range(4):
            x = random.randint(50, WINDOW_W-50)
            y = random.randint(50, WINDOW_H-50)
            enemies.add(hero.Hero('ghost.png', x, y, 50, 50, 5))

    pygame.display.update()
    clock.tick(40)

""" 
доделать анимацию пакмана
"""
