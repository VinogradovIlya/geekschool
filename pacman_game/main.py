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

player = hero.Hero('pacman_open.png', WINDOW_W/2-200, WINDOW_H/2, 50, 50, 0)
barriers = pygame.sprite.Group()
for x in range(0, WINDOW_W, 50):
    barriers.add(sprite.GameSprite('wall.jpg', x, 0, 50, 50))
    barriers.add(sprite.GameSprite('wall.jpg', x, WINDOW_H-50, 50, 50))
for y in range(0, WINDOW_H, 50):
    barriers.add(sprite.GameSprite('wall.jpg', 0, y, 50, 50))
    barriers.add(sprite.GameSprite('wall.jpg', WINDOW_W-50, y, 50, 50))
barriers.add(sprite.GameSprite('wall.jpg', WINDOW_H/2, WINDOW_H/2, 50, 50))
barriers.add(sprite.GameSprite('wall.jpg', WINDOW_H/2-50, WINDOW_H/2, 50, 50))
barriers.add(sprite.GameSprite('wall.jpg', WINDOW_H/2+50, WINDOW_H/2, 50, 50))
barriers.add(sprite.GameSprite('wall.jpg', WINDOW_H/2, WINDOW_H/2-50, 50, 50))
barriers.add(sprite.GameSprite('wall.jpg', WINDOW_H/2, WINDOW_H/2+50, 50, 50))

running = True
left = False
right = False
up = False
down = False
while running:
    mw.fill(BACK)
    enemies.draw(mw)
    barriers.draw(mw)
    player.reset(mw)
    player.update(barriers, WINDOW_W, WINDOW_H)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                player.x_speed = -5
            elif e.key == pygame.K_d:
                player.x_speed = 5
            elif e.key == pygame.K_w:
                player.y_speed = -5
            elif e.key == pygame.K_s:
                player.y_speed = 5
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_a:
                player.x_speed = 0
            elif e.key == pygame.K_d:
                player.x_speed = 0
            elif e.key == pygame.K_w:
                player.y_speed = 0
            elif e.key == pygame.K_s:
                player.y_speed = 0

    pygame.display.update()
    clock.tick(40)
