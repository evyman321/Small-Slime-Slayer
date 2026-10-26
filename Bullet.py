import pygame
from assets.Code import Settings

class Bullet:
    def __init__(self, x, y, direction):
        self.direction = direction
        self.worldX = x
        self.worldY = y
        self.initialX = x
        self.initialY = y
        self.vel = 20
        self.damage = 10
        self.alive = True
        self.hitbox = pygame.Rect(self.worldX - 2, self.worldY - 2, 4, 4)

    def update(self):
        match self.direction:
            case 'U':
                self.worldY -= self.vel
            case 'UL':
                self.worldY -= self.vel*0.707
                self.worldX -= self.vel*0.707
            case 'UR':
                self.worldY -= self.vel*0.707
                self.worldX += self.vel*0.707
            case 'D':
                self.worldY += self.vel
            case 'DL':
                self.worldY += self.vel*0.707
                self.worldX -= self.vel*0.707
            case 'DR':
                self.worldY += self.vel*0.707
                self.worldX += self.vel*0.707
            case 'L':
                self.worldX -= self.vel
            case 'R':
                self.worldX += self.vel
        
        self.hitbox = pygame.Rect(self.worldX - 2, self.worldY - 2, 4, 4)
        if abs(self.worldX - self.initialX) + abs(self.worldY - self.initialY) >= 50*Settings.TILESIZE:
            self.alive = False

    def draw(self, screen):
        screenX = Settings.WorldMapStartingX + self.worldX
        screenY = Settings.WorldMapStartingY + self.worldY
        pygame.draw.circle(screen, (200, 0, 0), (screenX, screenY), 2)
