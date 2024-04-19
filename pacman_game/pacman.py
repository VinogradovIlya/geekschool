import hero
import pygame


class Player(hero.Hero):
    def __init__(self, player_image, x, y, w, h, speed):
        super().__init__(self, player_image, x, y, w, h)
        self.x_speed = speed
        self.y_speed = speed

    
