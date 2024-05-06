from typing import override
import hero
import pygame


class Pacman(hero.Hero):
    def __init__(self, player_image, x, y, w, h, player_speed):
        super().__init__(player_image, x, y, w, h, player_speed)
        self.anim = [
            pygame.transform.scale(
                pygame.image.load('pacman1.png'), (self.rect.w, self.rect.h)),
            pygame.transform.scale(
                pygame.image.load('pacman2.png'), (self.rect.w, self.rect.h)),
            pygame.transform.scale(
                pygame.image.load('pacman3.png'), (self.rect.w, self.rect.h))]
        self.image = self.anim[2]
        self.frame = 0  # текущий кадр
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 150  # как быстро кадры меняются

    def animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
            self.image = self.anim[self.frame]

    @override
    def move(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                self.left = True
            elif e.key == pygame.K_RIGHT:
                self.right = True
            elif e.key == pygame.K_UP:
                self.up = True
            elif e.key == pygame.K_DOWN:
                self.down = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                self.left = False
            elif e.key == pygame.K_RIGHT:
                self.right = False
            elif e.key == pygame.K_UP:
                self.up = False
            elif e.key == pygame.K_DOWN:
                self.down = False

    @override
    def outside(self, w, h):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > h:
            self.rect.bottom = h
        elif self.rect.right > w:
            self.rect.right = w
        elif self.rect.left < 0:
            self.rect.left = 0
