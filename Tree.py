import pygame
from assets.Code import Object, Settings

class Tree(Object.Object):
    def __init__(self, worldX, worldY):
        super().__init__(worldX, worldY)
        self.worldX = worldX
        self.worldY = worldY
        self.image = Settings.TREE_IMG
        self.solid = True
        self.shadow = Settings.TREE_SHADOW
        self.shadowX = 12
        self.shadowY = 56
        self.hitbox = pygame.Rect(self.shadowX + 11, self.shadowY, 22, 8)

    def draw(self, screen):
        screenX = Settings.WorldMapStartingX + self.worldX
        screenY = Settings.WorldMapStartingY + self.worldY
        screen.blit(self.shadow, (screenX + self.shadowX, screenY + self.shadowY))
        screen.blit(self.image, (screenX, screenY))
