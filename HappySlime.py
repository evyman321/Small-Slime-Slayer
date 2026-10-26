import pygame
import random
from assets.Code import Settings, CollisionChecker, Bullet

class HappySlime:
    def __init__(self, player):
        self.downImages = Settings.HAPPY_SLIME_IMAGES[0:5]
        self.upImages = Settings.HAPPY_SLIME_IMAGES[5:]
        self.currentImages = self.downImages
        self.image = self.downImages[0]
        self.shadowIMG = Settings.SLIME_SHADOW
        
        self.player = player
        
        self.spawnRadius = Settings.TILESIZE*12
        self.noSpawnRadius = Settings.TILESIZE*7
        
        self.chaseRadius = Settings.TILESIZE*8

        self.worldX = self.getSpawnX()
        self.worldY = self.getSpawnY()
        
        self.shadowX = 0
        self.shadowY = 16

        self.damage = 5
        self.health = 75
        self.knockback = 30

        self.direction = 'I'
        self.spriteNum = 0
        self.spriteCounter = 0
        self.spriteCounterMax = Settings.FPS/5
        
        self.dirChangeCounter = 0
        self.dirChangeCounterMax = random.randint(Settings.FPS*3, Settings.FPS*10)

        self.vel = 2
        self.chasing = False

        self.colliding = False
        self.hitbox = pygame.Rect(self.shadowX, self.shadowY, 20, 20)

        self.alive = True

    def getSpawnableTiles(self):
        return [10]

    def getSpawnX(self):
        return self.player.worldX + random.choice([random.randint(-self.spawnRadius, -self.noSpawnRadius), random.randint(self.noSpawnRadius, self.spawnRadius)])

    def getSpawnY(self):
        return self.player.worldY + random.choice([random.randint(-self.spawnRadius, -self.noSpawnRadius), random.randint(self.noSpawnRadius, self.spawnRadius)])

    def changeDir(self):
        self.chasing = False
        if self.dirChangeCounter >= self.dirChangeCounterMax:
            self.dirChangeCounter = 0
            self.direction = random.choice(('U', 'D', 'L', 'R', 'I'))
            
        if abs(self.player.worldX - self.worldX) <= self.chaseRadius and abs(self.player.worldY - self.worldY) <= self.chaseRadius:
            self.chasing = True
            if abs(self.player.worldY - self.worldY) <= self.chaseRadius/2 and not self.player.worldX == self.worldX:
                self.direction = 'R' if self.player.worldX >= self.worldX else 'L'
            else:
                self.direction = 'D' if self.player.worldY >= self.worldY else 'U'
        
    def checkCollision(self):
        self.colliding = False
        CollisionChecker.checkObjects(self)
        Hitbox = self.hitbox.move(self.worldX, self.worldY)

        for bullet in self.player.bullets:
            if Hitbox.colliderect(bullet.hitbox):
                self.health -= bullet.damage
                self.player.bullets.remove(bullet)

        if self.health < 0:
            self.player.kills += 1
            self.alive = False
        
    def move(self):
        self.dirChangeCounter += 1
        if not self.colliding:
            match self.direction:
                case 'U':
                    self.worldY -= self.getCurrentVelY()
                case 'D':
                    self.worldY += self.getCurrentVelY()
                case 'L':
                    self.worldX -= self.getCurrentVelX()
                case 'R':
                    self.worldX += self.getCurrentVelX()

    def attack(self):
        playerHitbox = self.player.hitbox.move(self.player.worldX, self.player.worldY)
        enemyHitbox = self.hitbox.move(self.worldX, self.worldY)
        if enemyHitbox.colliderect(playerHitbox):
            self.player.health -= self.damage
            if self.worldX <= self.player.worldX:
                Settings.WorldMapStartingX -= self.knockback
                self.player.worldX += self.knockback
            else:
                Settings.WorldMapStartingX += self.knockback
                self.player.worldX -= self.knockback

    def getCurrentVelX(self):
        return self.vel if not self.chasing else min(self.vel, abs(self.player.worldX - self.worldX))

    def getCurrentVelY(self):
        return self.vel if not self.chasing else min(self.vel, abs(self.player.worldY - self.worldY))

    def updateSprite(self):
        self.spriteCounter += 1
        if self.spriteCounter >= self.spriteCounterMax:
            self.spriteCounter = 0
            self.spriteNum += 1
            if self.spriteNum >= 5:
                self.spriteNum = 0
            if self.direction == 'I' and self.spriteNum >= 2:
                self.spriteNum = 0
                
            match self.direction:
                case 'I':
                    self.image = self.currentImages[self.spriteNum]
                case 'U' | 'R':
                    self.image = self.upImages[self.spriteNum]
                    self.currentImages = self.upImages
                case 'D' | 'L':
                    self.image = self.downImages[self.spriteNum]
                    self.currentImages = self.downImages
    
    def update(self):
        self.changeDir()
        self.checkCollision()
        self.move()
        self.attack()
        self.updateSprite()

    def draw(self, screen):
        screenX = Settings.WorldMapStartingX + self.worldX
        screenY = Settings.WorldMapStartingY + self.worldY
        screen.blit(self.shadowIMG, (screenX + self.shadowX, screenY + self.shadowY))
        screen.blit(self.image, (screenX, screenY))
