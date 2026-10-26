import pygame
from paths import getPath

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360

FPS = 60
TILESIZE = 32
WorldMapStartingX = -(TILESIZE*53)
WorldMapStartingY = -(TILESIZE*64)

PLAYER_VEL = 3
GRAVITY = 0.5

#fonts
HEALTH_BAR_FONT = pygame.font.Font(getPath("assets", "Fonts", "ComicNeue-Bold.ttf"), 10)
DIALOGUE_FONT = pygame.font.Font(getPath("assets", "Fonts", "Silkscreen-Regular.ttf"), 25)

# images
DIALOGUE_SCREEN = pygame.image.load(getPath("assets", "images", "Dialogue Screen", "Dialogue Screen.png"))

PLAYER_IMAGES = []
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "down1.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "down2.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "down3.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "down4.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "up1.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "up2.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "up3.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "up4.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "right1.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "right2.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "right3.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "right4.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "left1.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "left2.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "left3.png")))
PLAYER_IMAGES.append(pygame.image.load(getPath("assets", "images", "Player", "left4.png")))

NPC_IMAGES = []
NPC_IMAGES.append(pygame.image.load(getPath("assets", "images", "objects", "idle1.png")))
NPC_IMAGES.append(pygame.image.load(getPath("assets", "images", "objects", "idle2.png")))
NPC_IMAGES.append(pygame.image.load(getPath("assets", "images", "objects", "idle3.png")))

HAPPY_SLIME_IMAGES = []
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "down1.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "down2.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "down3.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "down4.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "down5.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "up1.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "up2.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "up3.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "up4.png")))
HAPPY_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Happy Slime", "up5.png")))

MAD_SLIME_IMAGES = []
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "down1.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "down2.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "down3.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "down4.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "down5.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "down6.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "down7.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "up1.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "up2.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "up3.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "up4.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "up5.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "up6.png")))
MAD_SLIME_IMAGES.append(pygame.image.load(getPath("assets", "images", "Enemies", "Mad Slime", "up7.png")))

TREE_IMG = pygame.image.load(getPath("assets", "images", "objects", "tree.png"))

TREE_SHADOW = pygame.image.load(getPath("assets", "images", "Shadows", "Tree Shadow.png"))
PLAYER_SHADOW = pygame.image.load(getPath("assets", "images", "Shadows", "Player Shadow.png"))
SLIME_SHADOW = pygame.image.load(getPath("assets", "images", "Shadows", "Slime Shadow.png"))

GRASS_IMG = pygame.image.load(getPath("assets", "images", "tiles", "grass.png"))
SOLID_GRASS_IMG = pygame.image.load(getPath("assets", "images", "tiles", "solid grass.png"))

