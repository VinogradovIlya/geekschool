from typing import override
import hero
import pygame


class Pacman(hero.Hero):
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