import sprite
import pygame


class Hero(sprite.GameSprite):
    def __init__(self, player_image, x, y, w, h, player_speed):
        super().__init__(player_image, x, y, w, h)
        self.y_speed = player_speed
        self.x_speed = player_speed

    def move_up(self):
        self.y_speed = 5

    def move_down(self):
        self.y_speed = -5

    def move_left(self):
        self.x_speed = -5

    def move_right(self):
        self.x_speed = 5

    def update(self, walls, w, h):
        if self.rect.x <= w-80 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if self.rect.y <= h-80 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
