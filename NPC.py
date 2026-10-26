import pygame
from assets.Code import Object, Settings, DialogueHandler

class NPC(Object.Object):
    def __init__(self, worldX, worldY, screen):
        super().__init__(worldX, worldY)
        self.screen = screen
        self.worldX = worldX
        self.worldY = worldY
        self.images = Settings.NPC_IMAGES
        self.image = self.images[0]
        self.spriteNum = 0
        self.spriteCounter = 0
        self.spriteCounterMax = Settings.FPS/2
        self.solid = True
        self.shadow = Settings.TREE_SHADOW
        self.shadowX = -3
        self.shadowY = 16
        self.messages = ["You Are A Worthless Guy", "You Can Never Prove Me Wrong", "Look At Ur Tiny Little\nBody? U Think U Can Slay Slimes\n With That?", "Good Luck Cuz Ur Gonna Need It!"]
        self.hitbox = pygame.Rect(self.shadowX + 11, self.shadowY, 11, 4)
        self.onInteraction()

    def update(self):
        self.spriteCounter += 1
        if self.spriteCounter >= self.spriteCounterMax:
            self.spriteCounter = 0
            self.spriteNum += 1
            if self.spriteNum >= 3:
                self.spriteNum = 0
            self.image = self.images[self.spriteNum]

    def draw(self, screen):
        screenX = Settings.WorldMapStartingX + self.worldX
        screenY = Settings.WorldMapStartingY + self.worldY
        screen.blit(self.shadow, (screenX + self.shadowX, screenY + self.shadowY))
        screen.blit(self.image, (screenX, screenY))

    def onInteraction(self):
        DialogueHandler.drawDialogueScreen(self.screen, self.messages)
