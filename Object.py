import pygame

class Object:
    def __init__(self, worldX, worldY):
        self.worldX = worldX
        self.worldY = worldY
        self.hitbox = pygame.Rect(0, 0, 0, 0)
        self.solid = False

    def onCollision(self):
        pass

    def onInteraction(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
