import pygame

class Cutscene:
    def __init__(self, screen, images):
        self.screen = screen
        self.animationImages = images

    def animate(self):
        for image in images:
            screen.blit(image, (0, 0))
