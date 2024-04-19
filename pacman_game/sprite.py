import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, x, y, w, h):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(player_image), (w, h))
        self.rect = pygame.Rect(x, y, w, h)

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
