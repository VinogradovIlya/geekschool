import sprite
import random


class Hero(sprite.GameSprite):
    def __init__(self, player_image, x, y, w, h, player_speed):
        super().__init__(player_image, x, y, w, h)
        self.speed = player_speed
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.direction = random.randint(0,3)

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def outside(self, w, h):
        if self.rect.top < 0:
            self.rect.top = 0
            self.direction = 3
        elif self.rect.bottom > h:
            self.rect.bottom = h
            self.direction = 2
        elif self.rect.right > w:
            self.rect.right = w
            self.direction = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.direction = 1

    def direct(self):
        direct = random.randint(0, 3)
        if self.direction == direct:
            while self.direction == direct:
                direct = random.randint(0, 3)
        self.direction = direct

    def move(self, number):
        if number == 0:
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        if number == 1:
            self.left = False
            self.right = True
            self.up = False
            self.down = False
        if number == 2:
            self.left = False
            self.right = False
            self.up = True
            self.down = False
        if number == 3:
            self.down = True
            self.left = False
            self.right = False
            self.up = False
        if self.left:
            self.move_left()
        if self.right:
            self.move_right()
        if self.up:
            self.move_up()
        if self.down:
            self.move_down()
