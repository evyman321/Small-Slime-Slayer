import pygame
from assets.Code import Settings, CollisionChecker, ObjectHandler, Bullet

class Player:
    def __init__(self, entities):
        self.entities = entities
        self.bullets = []
        self.spriteCounter = 0
        self.spriteNum = 0
        self.spriteCounterMax = Settings.FPS/5
        self.direction = 'D'
        self.moving = False
        self.ammo = 5

        images = Settings.PLAYER_IMAGES
        self.downImages = images[0:4]
        self.upImages = images[4:8]
        self.rightImages = images[8:12]
        self.leftImages = images[12:]
        self.image = self.downImages[self.spriteNum]
        self.shadowImage = Settings.PLAYER_SHADOW
        
        self.size = 16
        self.vel = Settings.PLAYER_VEL
        self.kills = 0
        
        self.x, self.y = Settings.SCREEN_WIDTH/2 - self.size/2, Settings.SCREEN_HEIGHT/2 - self.size/2
        self.worldX, self.worldY = self.x - Settings.WorldMapStartingX, self.y - Settings.WorldMapStartingY
        self.shadowX, self.shadowY = 3, 14

        self.totalHealth = 100
        self.health = 100
        
        self.hitbox = pygame.Rect(self.shadowX, self.shadowY, 8, 6)
        self.colliding = False

        self.lose = False
        self.win = False

    def draw(self, screen):
        screen.blit(self.shadowImage, (self.x + 3, self.y + 14))
        screen.blit(self.image, (self.x, self.y))

    def drawHealthBar(self, screen):
        healthbar = pygame.draw.rect(screen, (150, 0, 0), (self.x + self.size/2 - 25, self.y - 20, self.totalHealth/2, 10))
        pygame.draw.rect(screen, (0, 150, 0), (self.x + self.size/2 - 25, self.y - 20, self.health/2, 10))
        text = Settings.HEALTH_BAR_FONT.render(f"{self.health}/{self.totalHealth}", True, (200, 200, 200))
        textRect = text.get_rect()
        textRect.center = healthbar.center
        screen.blit(text, (textRect.x, textRect.y))
        
    def updateSprite(self):
        self.spriteCounter += 1
        if self.spriteCounter >= self.spriteCounterMax:
            self.spriteCounter = 0
            self.spriteNum += 1
            if self.spriteNum >= 4:
                self.spriteNum = 0

        if not self.moving and self.spriteNum == 1:
            self.spriteNum = 0

        match self.direction:
            case 'U'|'UL'|'UR':
                self.image = self.upImages[self.spriteNum]
            case 'D'|'DL'|'DR':
                self.image = self.downImages[self.spriteNum]
            case 'L':
                self.image = self.leftImages[self.spriteNum]
            case 'R':
                self.image = self.rightImages[self.spriteNum]

    def changeDir(self):
        keys =  pygame.key.get_pressed()
        self.moving = False
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.direction = 'L'
            self.moving = True
        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.direction = 'R'
            self.moving = True
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.direction = 'U'
            if keys[pygame.K_a] and not keys[pygame.K_d]:
                self.direction = 'UL'
            if keys[pygame.K_d] and not keys[pygame.K_a]:
                self.direction = 'UR'
            self.moving = True
        if keys[pygame.K_s] and not keys[pygame.K_w]:
            self.direction = 'D'
            if keys[pygame.K_a] and not keys[pygame.K_d]:
                self.direction = 'DL'
            if keys[pygame.K_d] and not keys[pygame.K_a]:
                self.direction = 'DR'
            self.moving = True
        if keys[pygame.K_RETURN]:
            if self.ammo - len(self.bullets) > 0:
                bullet = Bullet.Bullet(self.worldX, self.worldY, self.direction)
                self.bullets.append(bullet)

    def getCurrentVelX(self):
        return self.vel

    def getCurrentVelY(self):
        return self.vel

    def checkCollision(self):
        self.colliding = False
        CollisionChecker.checkObjects(self, True)

    def drawKills(self, screen):
        pass
       
    def move(self):
        if self.moving and not self.colliding:
            match self.direction:
                case 'U':
                    Settings.WorldMapStartingY += self.getCurrentVelY()
                case 'UL':
                    Settings.WorldMapStartingY += self.getCurrentVelY()*0.707
                    Settings.WorldMapStartingX += self.getCurrentVelX()*0.707
                case 'UR':
                    Settings.WorldMapStartingY += self.getCurrentVelY()*0.707
                    Settings.WorldMapStartingX -= self.getCurrentVelX()*0.707
                case 'D':
                    Settings.WorldMapStartingY -= self.getCurrentVelY()
                case 'DL':
                    Settings.WorldMapStartingY -= self.getCurrentVelY()*0.707
                    Settings.WorldMapStartingX += self.getCurrentVelX()*0.707
                case 'DR':
                    Settings.WorldMapStartingY -= self.getCurrentVelY()*0.707
                    Settings.WorldMapStartingX -= self.getCurrentVelX()*0.707
                case 'L':
                    Settings.WorldMapStartingX += self.getCurrentVelX()
                case 'R':
                    Settings.WorldMapStartingX -= self.getCurrentVelX()

    def updateWorldPos(self):
        self.worldX, self.worldY = self.x - Settings.WorldMapStartingX, self.y - Settings.WorldMapStartingY

    def checkWinOrLose(self):
        if self.health < 0:
            self.lose = True
        elif self.kills >= 2:
            self.win = True
                    
    def update(self):
        self.changeDir()
        self.checkCollision()
        self.move()
        self.updateSprite()
        self.updateWorldPos()
        self.checkWinOrLose()

        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)
