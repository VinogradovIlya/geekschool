import pygame
import hero
import sprite
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

player = pacman.Pacman('pacman_open.png', WINDOW_W/2, WINDOW_H/2, 50, 50, 10)

running = True
start = time.time()
direction = [random.randint(0, 3) for _ in range(4)]
while running:
    now = time.time()
    if now - start >= 5:
        direction = [random.randint(0, 3) for _ in range(4)]
        start = now
    for e, num in zip(enemies, direction):
        e.move(num)
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

    pygame.display.update()
    clock.tick(40)

""" 
доделать движение монстриков
доделать анимацию пакмана
"""
